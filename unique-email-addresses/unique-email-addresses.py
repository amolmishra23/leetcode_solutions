class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            res.add(local+'@'+domain)
            
        return len(res)