#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#


# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        dests = []
        for email in emails:
            splitted = email.split("@")
            local = splitted[0]
            domain = splitted[1]
            # localを整形
            local_after = local.replace(".", "").split("+")[0]
            # 判定
            mail_after = local_after + "@" + domain
            if mail_after not in dests:
                count += 1
                dests.append(mail_after)
        return count


# @lc code=end
