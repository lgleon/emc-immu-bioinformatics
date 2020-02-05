import os

# stripe keys
os.environ.setdefault("STRIPE_PUBLISHABLE", "pk_test_NMgLaBTQQP5QQALzQcEWXmJa00gRpILmoP")
os.environ.setdefault("STRIPE_SECRET", "sk_test_xa53Ub9W3pk6EMWEHHuzmEKw00eftux3gR")





"""
LETY ACUERDATE QUE HAS QUITADO DE AQUI LA SECRET KEY THE POSTGRESS, HEROKU PUEDE DAR PROBLEMAS !!!!!

"""





#my secret key I cannot hide because import env is not workin
#well it seems to work but travis through and error because cannot find the key
os.environ.setdefault("SECRET_KEY", '22ioik$lorgg4*@m+uqqw73+8okqe5#sj$z%^%+uoonk1rhx@9')
