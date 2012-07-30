from txcron.protocol import task, cron_start
@task("*/1 * * * *")
def lala(lele):
    print(lele)

if __name__ == "__main__":
    cron_start() 
