class Logger:
    def log(self,error=None,warning=None,info=None):
        print(f"error: {error}\nwarning: {warning}\ninfo: {info}")
logger1=Logger()
logger1.log('error','no warning','sample test')
logger2=Logger()
logger2.log('no error')