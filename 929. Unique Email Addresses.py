#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def numUniqueEmails(emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        sentmail = []
        for email in emails:
            email = email.split('@')
            if '+' in email[0]:
                email[0] = email[0][:email[0].index("+")]
            if '+' in email[1]:
                email[1] = email[1][:email[1].index("+")]
            email[0] = email[0].replace('.','')
            email = '@'.join(email)
            if email not in sentmail:
                sentmail.append(email)
        return len(sentmail)
        
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Solution.numUniqueEmails(emails)

