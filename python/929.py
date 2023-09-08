class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = {}

        for e in emails:
            if e.find('@') == -1:
                continue
            
            local, domain = e.split('@')
            local = "".join(local.split('.'))
            if local.find('+') != -1:
                local = local.split('+')[0]

            unique[local + '@' + domain] = True

        return len(unique.keys())
    
