# this is a mixin containing only methods but it holds unnecessary methods
# we solve by spreading it to 4 classes Interface segregation
class EntertainmentDevice:
    # def connect_to_device_via_hdmi_cable(self, device): pass
    #
    # def connect_to_device_via_rca_cable(self, device): pass
    #
    # def connect_to_device_via_ethernet_cable(self, device): pass

    # every console has a power outlet
    def connect_device_to_power_outlet(self, device): pass


# SRP every connector has his own cable but also
# LSP every connector knows how to connect to power outlet
class HDMIConnector(EntertainmentDevice):
    def connect_device_via_hmi_cable(self, device): pass


class RCAConnector(EntertainmentDevice):
    def connect_to_device_via_rca_cable(self, device): pass


class EthernetConnector(EntertainmentDevice):
    def connect_to_device_via_ethernet_cable(self, device): pass


# now devices can only contain knowledge about the methods they can use ISP
class Television(HDMIConnector, RCAConnector):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMIConnector, EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(HDMIConnector, EthernetConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EthernetConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
