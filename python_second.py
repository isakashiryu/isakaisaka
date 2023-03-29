# emailアドレス email とドメイン名 domain を引数に取って、email のドメイン名を domain に置き換える関数 change_domain(email, domain) を作成してください。 なお、emailアドレスのドメイン名とは、 '@' で区切られた右側の部分を意味します。
# 次のセルの ... のところを書き換えて change_domain(email, domain) を完成させてください。
def change_domain(email, domain):
    return '@'.join([email.split('@')[0], domain])