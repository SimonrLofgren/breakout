class Looper:
    def __init__(self, main_menu, p1_menu, running, in_level):
        self.main_menu = main_menu
        self.p1_menu = p1_menu
        self.running = running
        self.in_level = in_level

    def set_main_menu(self, x):
        """

        :param x: Bool
        :return: None
        """
        self.main_menu = x

    def set_p1_menu(self, x):
        """

        :param x: Bool
        :return: None
        """
        self.p1_menu = x

    def set_running(self, x):
        """

        :param x: Bool
        :return: None
        """
        self.running = x

    def set_in_level(self, x):
        """

        :param x: Bool
        :return: None
        """
        self.in_level = x

    def quit(self):
        self.main_menu = False
        self.running = False
        self.in_level = False
        self.p1_menu = False