def change_domain(email, domain):
    return '@'.join([email.split('@')[0], domain])

# 使用例
old_email = 'seino.kaimu@icloud.com.com'
new_domain = 'newdomain.com'

new_email = change_domain(old_email, new_domain)
print(new_email) # seino.kaimu@icloud.com