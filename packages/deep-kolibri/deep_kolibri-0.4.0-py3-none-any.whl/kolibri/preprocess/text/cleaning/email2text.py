# -*- coding: utf-8 -*-
# !/usr/bin/env python

import re
import collections
from kolibri.preprocess.text.cleaning.cleaning_scripts import fix_formating
from kolibri.preprocess.text.cleaning.__email_configs import *
import eml_parser
from math import sqrt
import gcld3, glob
from os.path import isfile, join
from tqdm import tqdm
import os


lang_detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0,
                                             max_num_bytes=1000)

class EmailMessage(object):
    """
    An email message represents a parsed email body.
    """

    def __init__(self, language='en', split_pattern=None, remove_html=True, escape_rejected_emails=True):
        self.fragments = []
        self.fragment = None
        self.found_visible = False
        self.language = language
        self.salutations = [s.strip() for s in open(filename_salutation).readlines() if s.strip() != ""]

        self.split_pattern = split_pattern
        self.regex_header = r"|".join(regex_headers)
        self.title=None
        self.email_parser=None
        self.parsed_data={}
        self.remove_html=remove_html
        self.escape_rejected_emails=escape_rejected_emails

    def read(self, body_text, title_text=None):
        """ Creates new fragment for each line
            and labels as a signature, quote, or hidden.
            Returns EmailMessage instance
        """
        self.fragments = []
        self.title=title_text
        body_text=fix_formating(str(body_text))
        if self.remove_html:
            body_text=re.sub(r'(<|\[)https?:\/\/.*(\.).*(>|\])', '',body_text)
        if self.escape_rejected_emails:
            for rejection in rejected_emails_formulas:
                if rejection.strip() in body_text:
                    body_text="[EMAIL_REJECTED]"
                    break

        self.text = body_text

        self.title = title_text
        #        regex_header = r"(From|To)\s*:[0-9A-Za-zöóìśćłńéáú⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎\s\/@\.:,;\&\?\\\(\)'\"\*[\]<>#\/\+_-]+?((Subj(ect)?)|Sent at)\s?:|From\s*:[\w @\.:,;\&\(\)'\"\*[\]<>#\/\+-]+?(Sent|Date)\s?:(\s*\d+(\s|\/)(\w+|\d+)(\s|\/)\d+(\s|\/)?(\d+:\d+)?)?|From\s*:[\w @\.:,;\&\(\)'\"\*[\]<>#\/\+-]+?(Sent\s+at)\s?:(\s*\d+\s\w+\s\d+\s?\d+:\d+)?|From\s*:[\w @\.:,;\&\?\\\(\)'\"\*[\]<>#\/\+-]+?(CC)\s?:|From\s*:[\w @\.:,;\&\?\\\(\)'\"\*[\]<>#\/\+-]+?(To)\s?:|(De|Da)\s*:[0-9ÀA-Za-zéàçèêù\s\/@\.:,;\&\?\\\(\)'\"\*[\]<>#\/\+-]+(Objet|Oggetto)\s?:"
        if self.split_pattern:
            self.regex_header = r"" + self.split_pattern
        starts = [m.start(0) for m in re.finditer(self.regex_header, self.text, re.MULTILINE | re.UNICODE)]

        if len(starts) < 1:
            starts = [m.start(0) for m in re.finditer(pattern_salutation, self.text, re.MULTILINE)]
            starts = [s for s in starts if s > 150]
        if len(starts) < 1:
            self.fragments.append(Fragment(self.text, self.salutations, self.regex_header))

        else:
            if starts[0] > 0:
                starts.insert(0, 0)
            lines = [self.text[i:j] for i, j in zip(starts, starts[1:] + [None])]

            for line in lines:
                if self.split_pattern:
                    line = re.sub(self.split_pattern, '', line)
                if line.strip() != '':
                    self.fragments.append(Fragment(line, self.salutations, self.regex_header))

        return self

    def read_eml(self, eml_file):
        self.parsed_data=self.parse_eml(eml_file)
        self.read(self.parsed_data['body'], self.parsed_data['title'])
        return self

    def parse_eml(self, eml_file):

        with open(eml_file, 'rb') as fhdl:
            raw_email = fhdl.read()
        if self.email_parser is None:
            self.email_parser = eml_parser.EmlParser(include_raw_body=True)

        parsed_eml = self.email_parser.decode_email_bytes(raw_email)

        in_replay=""
        if 'in-reply-to' in parsed_eml['header']['header']:
            in_replay=parsed_eml['header']['header']['in-reply-to']

        attachements=[]
        if 'attachment' in parsed_eml:
            attachements=[att['filename'] for att in parsed_eml['attachment']]
        language=""
        if 'content-language' in parsed_eml['header']['header']:
            language=parsed_eml['header']['header']['content-language'][0]
        body=""
        references=""
        if 'message-id' in parsed_eml['header']['header']:
            references = parsed_eml['header']['header']['message-id']
        if len(parsed_eml['body']) > 0:
            body=parsed_eml['body'][0]['content']

        return{
            "body": body,
            "title": parsed_eml['header']['subject'],
            "from": parsed_eml['header']['from'],
            "to": parsed_eml['header']['to'],
            "date": parsed_eml['header']['date'],
            "from_name": parsed_eml['header']['header']['from'][0],
            "language": language,
            'message-id':references,
            "in_replay_to":in_replay,
            "attachement_names":attachements
        }

    def detect_language(self):
        langs = [l.language for l in self.fragments]
        languages = collections.Counter()
        for d in langs:
            languages.update(d)
        if not languages:
            try:
                lang = lang_detector.FindTopNMostFreqLangs(self.title, num_langs=2)

            except:
                try:
                    lang = lang_detector.FindTopNMostFreqLangs(self.text, num_langs=2)
                except:
                    languages['und'] = 0.90

                    return languages

            for l in lang:
                languages[l.language] = l.probability
        self.language=max(languages, key=languages.get)
        return self.language


class Fragment(object):
    """ A Fragment is a part of
        an Email Message, labeling each part.
    """

    def __init__(self, email_text, salutations, regex_header):

        self.salutations = salutations
        self.body = email_text.strip()
        self.regex_header = regex_header
        self.is_forwarded_message = self._get_forwarded()
        self.title = None
        self.headers = self._get_header()
        self.caution = self._get_caution_or_front_content()
        if self.title is None:
            self.title = self._get_title()
        self.attachement = self._get_attachement()
        self.salutation = self._get_salutation()
        self.disclaimer = self._get_disclaimer()
        self.signature = self._get_signature()

        self._content = email_text

    def _get_title(self):
        patterns = [
            "(R[Ee]|F[Ww])\s?:\s?.+",
            ".*\s+(?=(Hi|Hello|Dear))"
        ]

        pattern = r'(?P<title>(' + '|'.join(patterns) + '))'
        groups = re.match(pattern, self.body)
        title = ""
        if groups is not None:
            if "title" in groups.groupdict().keys():
                title = groups.groupdict()["title"]
                self.body = self.body[len(title):].strip()
        return title

    def _get_caution_or_front_content(self):
        patterns =[c.strip() for c in email_caution_or_fron_content+sent_from_my_device if c.strip()]
#        pattern = r'(?P<caution>^\s*(' + r'|'.join(patterns) + '))'
        pattern=r'(?P<caution>^\s*(^\s*'+ r'|'.join(patterns)+'))'

        match = re.search(pattern, self.body)
        cautions = []
        while match:
            caution = match.group()
            cautions.append(caution)
            _span = match.span()
            self.body=self.body[_span[1]:]
            match = re.search(pattern, self.body)
#        start_with_closing=
        if len(cautions)==0:
            start_with_closing= re.match(signature_pattern_bis, self.body.strip())
            if start_with_closing:
                #we search for salution. if email start with closing, then form closing to salutation is to be removed
                match= re.search(pattern_salutation, self.body, re.MULTILINE)
                if match:
                    cautions = self.body[:match.start()]
                    self.body=self.body[match.start():]
            return cautions
        # groups = re.match(pattern, self.body, re.MULTILINE)
        # caution=""
        # if groups is not None:
        #     if "caution" in groups.groupdict().keys():
        #         caution = groups.groupdict()["caution"]
        #         self.body = self.body[len(caution):].strip()
        return '\n'.join(cautions)

    def _get_attachement(self):
        pattern = r'(?P<attachement>(^\s*[a-zA-Z0-9_,\. -]+\.(png|jpeg|docx|doc|xlsx|xls|pdf|pptx|ppt))|Attachments\s?:\s?([a-zA-Z0-9_,\. -]+\.(png|jpeg|docx|doc|xlsx|xls|pdf|pptx|ppt)))'
        groups = re.match(pattern, self.body, re.IGNORECASE)
        attachement = ''
        if not groups is None:
            if "attachement" in groups.groupdict().keys():
                attachement = groups.groupdict()["attachement"]
                self.body = self.body[len(attachement):].strip()
        return attachement

    def _get_salutation(self):
        # Notes on regex:
        # Max of 5 words succeeding first Hi/To etc, otherwise is probably an entire sentence

        groups = re.match(pattern_salutation, self.body)
        salutation = ''
        if groups is not None:
            if "salutation" in groups.groupdict().keys():
                salutation = groups.groupdict()["salutation"]
                self.body = self.body[len(salutation):].strip()
        return salutation

    @property
    def language(self):
        return_val = {}
        regx = "\*?-+\s+Sent\s+:.*\s+Received\s+:.*\s+Reply to\s:.*\s+Attachments\s+:.*\s+\*?-*|Dear Sender, thank you for your e-mail. I'll be out of office until.*|NO BODY.*|[^\w.,:\s]"
        text = self.body
        text = re.sub(regx, ' ', text.strip())

        if len(text.strip()) > 0:
            try:
                lang = lang_detector.FindTopNMostFreqLangs(text=text, num_langs=2)
                for l in lang:
                    return_val[l.language] = l.probability * sqrt(len(text))
            except:
                pass
            try:
                lx, v, lang_cld = gcld3.detect(text)
                langs = set(['zh' if 'zh-' in l[1] else l[1] for l in lang_cld])

                if {'ko', 'zh-cn'}.intersection(set(return_val.keys())) or {'ko', 'zh'}.intersection(langs):
                    return_val = {}
                    for l in lang_cld:
                        return_val[l[1]] = (l[2] / 100) * sqrt(len(text))
            except:
                pass

        return return_val

    def _get_header(self):
        #        regex = r"From\s*:[\w @\.:,;\&\?\\\(\)'\"\*[\]<>#\/\+-]+?(Subj(ect)?)\s?:|From\s*:[\w @\.:,;\&\(\)'\"\*[\]<>#\/\+-]+?(Sent|Date)\s?:(\s*\d+(\s|\/)(\w+|\d+)(\s|\/)\d+(\s|\/)?(\d+:\d+)?)?|From\s*:[\w @\.:,;\&\(\)'\"\*[\]<>#\/\+-]+?(Sent\s+at)\s?:(\s*\d+\s\w+\s\d+\s?\d+:\d+)?|From\s*:[\w @\.:,;\&\?\\\(\)'\"\*[\]<>#\/\+-]+?(CC)\s?:|From\s*:[\w @\.:,;\&\?\\\(\)'\"\*[\]<>#\/\+-]+?(To)\s?:"

        pattern = r"(?P<header_text>(" + self.regex_header + "))"

        groups = re.search(pattern, self.body)
        header_text = None
        if groups is not None:
            if "header_text" in groups.groupdict().keys():
                header_text = groups.groupdict()["header_text"]
                self.body = self.body[len(header_text):].strip()
            if 'subject' in groups.groupdict().keys():
                self.title = groups.groupdict()["subject"]
        return header_text

    def _get_disclaimer(self):

        groups = re.search(pattern_disclaimer, self.body, re.MULTILINE + re.DOTALL)
        disclaimer_text = None
        if groups is not None:
            if "disclaimer_text" in groups.groupdict().keys():
                found = groups.groupdict()["disclaimer_text"]
                disclaimer_text = self.body[self.body.find(found):]
                self.body = self.body[:self.body.find(disclaimer_text)].strip()

        return disclaimer_text

    def _get_signature(self):
        # note - these openinged statements *must* be in lower case for
        # sig within sig searching to work later in this func

        # TODO DRY
        self.signature = ''

        groups = re.search(signature_pattern, self.body, re.IGNORECASE | re.MULTILINE)
        signature = None
        if groups:
            if "signature" in groups.groupdict().keys():
                signature1 = groups.groupdict()["signature"]
                # search for a sig within current sig to lessen chance of accidentally stealing words from body
                sig_span = groups.span()
                signature = self.body[sig_span[0]:]
                self.body = self.body[:sig_span[0]]
                groups = re.search(signature_pattern, signature[len(signature1):], re.IGNORECASE|re.MULTILINE)
                if groups:
                    signature2 = groups.groupdict()["signature"]
                    sig_span = groups.span()
                    self.body = self.body + '\n' + signature[:len(signature1)+sig_span[0]]
                    signature = signature[len(signature1)+sig_span[0]:]
        return signature

    def _get_forwarded(self):

        pattern = '(?P<forward_text>([- ]* Forwarded Message [- ]*|[- ]* Forwarded By [- ]*|[- ]*Original Message[- ]*))'
        groups = re.search(pattern, self.body, re.DOTALL)
        forward = None
        if groups is not None:
            if "forward_text" in groups.groupdict().keys():
                forward = groups.groupdict()["forward_text"]

        if forward is not None:
            self.body = self.body.replace(forward, '')

        return forward is not None

    @property
    def content(self):
        return self._content.strip()

def get_input_files(dir_path, type):

    return glob.glob(join(dir_path, "*." + type))




def process_eml_from_folder():

    import xlsxwriter

    workbook = xlsxwriter.Workbook('/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/Octa+/octaplus.xlsx')
    worksheet = workbook.add_worksheet()

    files=get_input_files("/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/Octa+/data/", 'eml')

    worksheet.write(0, 0, "ContactId")
    worksheet.write(0, 1, "body")
    worksheet.write(0, 2, "title")
    worksheet.write(0, 3, "from")
    worksheet.write(0, 4, "to")
    worksheet.write(0, 5, "date")
    worksheet.write(0, 6, "from_name")
    worksheet.write(0, 7, "language")
    worksheet.write(0, 8, "references")
    worksheet.write(0, 9, "in_replay_to")
    worksheet.write(0, 10, "attachement_names")
    worksheet.write(0, 11, "clean_body")
    worksheet.write(0, 12, "detected_lang")


    i=1

    with tqdm(total=len(files), position=0, leave=True) as pbar:
        for  file in tqdm(files, position=0, leave=True):
            email=EmailMessage().read_eml(file)
            cleaned='\n'.join([f.title + '\n' + f.body for f in email.fragments])
#            print(cleaned)
#            print('-----------------------------------------------------------------------\n')
            parsed=email.parsed_data
            parsed["FileName"]=os.path.split(file)[1]
            worksheet.write(i, 0, parsed["FileName"])
            worksheet.write(i, 1, parsed["body"])
            worksheet.write(i, 2, parsed["title"])
            worksheet.write(i, 3, parsed["from"])
            worksheet.write(i, 4, ";".join([ p for p in parsed["to"]]))
            worksheet.write(i, 5, str(parsed["date"]))
            worksheet.write(i, 6, parsed["from_name"])
            worksheet.write(i, 7, parsed["language"])
            worksheet.write(i, 8, ";".join([r for r in parsed["message-id"]]))
            worksheet.write(i, 9, ";".join([r for r in parsed["in_replay_to"]]))
            worksheet.write(i, 10, ";".join([a for a in parsed["attachement_names"]]))
            worksheet.write(i, 11,  cleaned)
            worksheet.write(i, 12, email.detect_language())
            i+=1
            pbar.update()

    workbook.close()


if __name__ == "__main__":


    text="""Merci d'annuler votre proposition de contrat G311049
Jean-Pierre Marchand
Client 523375

"""
    e=EmailMessage().read(text)
    import pandas as pd
    import sys

    data=pd.read_excel("/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/Octa+/octaplus.xlsx", engine='openpyxl')

    for i, d in data.iterrows():
        if i%1000==0:
            print(i)
#            data.to_excel(
#                "/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/Octa+/octaplus_clean.xlsx", engine="openpyxl")

        ec = EmailMessage().read(d['body'])
        val = '\n'.join([f.title + '\n' + f.body for f in ec.fragments])
        data.at[i, 'clean_body']= val
        data.at[i, 'detected_lang']= ec.detect_language()


    data.to_excel("/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/Octa+/octaplus_clean.xlsx", engine='openpyxl')









