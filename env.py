import os

# stripe keys
os.environ.setdefault("STRIPE_PUBLISHABLE", "pk_test_NMgLaBTQQP5QQALzQcEWXmJa00gRpILmoP")
os.environ.setdefault("STRIPE_SECRET", "sk_test_xa53Ub9W3pk6EMWEHHuzmEKw00eftux3gR")

#postgres secret key for heroku, not using it
os.environ.setdefault("DATABASE_URL", "postgres://mpbodjnslvgswz:2bc0941f06e107d10ba8926a50fb9f2722fefe2ce183ebca7eed4fc8d8420d24@ec2-54-217-225-16.eu-west-1.compute.amazonaws.com:5432/deq89pfojee4il")

#my secret key I cannot hide because import env is not workin
#well it seems to work but travis through and error because cannot find the key
os.environ.setdefault("SECRET_KEY", '22ioik$lorgg4*@m+uqqw73+8okqe5#sj$z%^%+uoonk1rhx@9')



#AWS keys not using them, I am no using AWS as repository for static and prefer not to use for imgs
os.environ.setdefault("AWS_ACCESS_KEY_ID", "AKIA3WVLGF6YYGLPNI6L")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "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")
