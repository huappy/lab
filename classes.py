

class Television:
    '''
    This class defines an instance of a Television and its settings
    including its power(on or off), the current channel, and the current volume.
    '''
    MIN_channel: int = 0     # Minimum TV __channel
    MAX_channel: int = 3     # Maximum TV __channel

    MIN_volume: int = 0      # Minimum TV __volume
    MAX_volume: int = 2      # Maximum TV __volume

    def __init__(self):
        '''
        Defines the initial settngs of the Television
        
        :param self: This television's current settings.
        '''
        self.__channel: int = Television.MIN_channel
        self.__volume: int = Television.MIN_volume
        self.__on: bool = "False"

        pass

    def power(self):
        '''
        Acts as a power button. If the TV is off, the power button turns it on and vice versa
        
        :param self: This television's current settings.
        '''
        if self.__on =="False":
            self.__on = "True"
        else:
            self.__on = "False"

        pass

    def channel_up(self):
        '''
        Adds one to the channel based on what the channel is currently set to. 
        For example if the channel is currently at 1, calling the function would set it to 2
        If the channel is already at its maximum, it will return the channel to its minimum.
        
        :param self: This television's current settings.
        '''
        if self.__on == "True":
            if self.__channel == Television.MAX_channel:
                self.__channel = Television.MIN_channel
            else:
                self.__channel += 1
        else:
            pass
        
        pass

    def channel_down(self):
        '''
        Subtracts one from the channel based on what the channel is currently set to. 
        For example if the channel is currently at 2, calling the function would set it to 1
        If the channel is already at its minimum, it will return the channel to its maximum.
        
        :param self: This television's current settings.
        '''
        if self.__on == "True":
            if self.__channel == Television.MIN_channel:
                self.__channel = Television.MAX_channel
            else:
                self.__channel -= 1
        else:
            pass

        pass

    def volume_up(self):
        '''Adds one to the volume based on what the volume is currently set to. 
        For example if the volume is currently at 1, calling the function would set it to 2
        If the volume is already at its maximum, the function will not chanve the volume.
        
        :param self: This television's current settings.
        '''
        if self.__on == "True":
            if self.__volume == Television.MAX_volume:
                pass
            else:
                self.__volume += 1

        pass

    def volume_down(self):
        '''
        Subtracts one from the volume based on what the volume is currently set to. 
        For example if the volume is currently at 2, calling the function would set it to 1
        If the volume is already at its minimum, the function will not chanve the volume.
        
        :param self: This television's current settings.
        '''
        if self.__on == "True":
            if self.__volume == Television.MIN_volume:
                pass
            else:
                self.__volume -= 1

        pass

    def __str__(self):
        '''
        Gives the current status of the TV including power, channel, and volume.
        
        :param self: This television's current settings
        :return: The status of the TV.
        '''
        return f"TV status: Is on = {self.__on}, channel = {self.__channel}, volume = {self.__volume}"

        pass
