class Television:
    MIN_channel: int = 0     # Minimum TV __channel
    MAX_channel: int = 3     # Maximum TV __channel

    MIN_volume: int = 0      # Minimum TV __volume
    MAX_volume: int = 2      # Maximum TV __volume

    def __init__(self):

        self.__channel: int = Television.MIN_channel
        self.__volume: int = Television.MIN_volume
        self.__on: bool = "False"

        pass

    def power(self):
        if self.__on =="False":
            self.__on = "True"
        else:
            self.__on = "False"

        pass

    def channel_up(self):
        if self.__on == "True":
            if self.__channel == Television.MAX_channel:
                self.__channel = Television.MIN_channel
            else:
                self.__channel += 1
        else:
            pass
        
        pass

    def channel_down(self):
        if self.__on == "True":
            if self.__channel == Television.MIN_channel:
                self.__channel = Television.MAX_channel
            else:
                self.__channel -= 1
        else:
            pass

        pass

    def volume_up(self):
        if self.__on == "True":
            if self.__volume == Television.MAX_volume:
                pass
            else:
                self.__volume += 1

        pass

    def volume_down(self):
        if self.__on == "True":
            if self.__volume == Television.MIN_volume:
                pass
            else:
                self.__volume -= 1

        pass

    def __str__(self):
        
        return f"TV status: Is on = {self.__on}, channel = {self.__channel}, volume = {self.__volume}"

        pass
