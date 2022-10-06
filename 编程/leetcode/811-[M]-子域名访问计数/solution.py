from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_cnt = {}
        for cp in cpdomains:
            cnt, domain = cp.split()
            domain = domain.split('.')
            for i in range(len(domain)):
                sub_domain = '.'.join(domain[len(domain)-i-1:])
                domain_cnt.setdefault(sub_domain, 0)
                domain_cnt[sub_domain] += int(cnt)
        return ['{} {}'.format(domain_cnt[domain], domain) for domain in domain_cnt]


if __name__ == '__main__':
    test = Solution()
    print(test.subdomainVisits(["9001 discuss.leetcode.com"]))
    print(test.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
            
