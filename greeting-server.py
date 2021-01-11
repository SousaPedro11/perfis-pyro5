import Pyro5.api
import Pyro5.server


@Pyro5.api.expose
class GreetingMaker(object):
    class Meta:
        verbose_name = "GreetingMaker"
        verbose_name_plural = "GreetingMakers"

    def get_fortune(self, name):
        return f"Olá, {name}. Aqui está sua fortuna: \n" \
               f"Sem nada, Liso!"


daemon = Pyro5.server.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(GreetingMaker)
ns.register('example.greeting', uri)

print(f"Pronto! Object uri = {uri}")
daemon.requestLoop()
