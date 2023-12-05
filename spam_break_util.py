CLEAN_HEADER = """
Subject: Example Subject
Message-ID: <GTUBE1.1010101@example.net>
Date: Wed, 23 Jul 2003 23:30:00 +0200
From: Sender <sender@example.net>
To: Recipient <recipient@example.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
"""

"""
Add a header to any text file.
"""
def add_clean_header(text):
    header_dict = {head: head + ": " + val for head, val in [x.split(": ") for x in CLEAN_HEADER.split('\n') if ": " in x]}
    text_arr = text.split('\n')

    text_subject = None
    remove_idx = None
    for i, x in enumerate(text_arr):
        if "subject:" in x.lower():
            text_subject = x
            remove_idx = i
            break

    if text_subject != None:
        header_dict['Subject'] = text_subject
        text_arr.pop(remove_idx)

    new_header = "\n".join([x for x in header_dict.values()])
    new_text = "\n".join(text_arr)
    
    return new_header + "\n\n" + new_text