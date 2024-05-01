class Ticket:
    def __init__(self) -> None:
        self.__file_type: str = None
        self.__file_type_version: str = None

        self.__device_type: str = None
        self.__uid: str = None
        self.__st25tb_data_type: str = None

        self.__block_matrix: list[str] = []
        self.__system_otp_block: str = None
        return
    

    def set_file_type(self, __file_type: str) -> None:
        self.__file_type = __file_type
        return
    

    def set_file_type_version(self, __file_type_version: str) -> None:
        self.__file_type_version = __file_type_version
        return
    
    
    def set_device_type(self, __device_type: str) -> None:
        self.__device_type = __device_type
        return
    
    
    def set_uid(self, __uid: str) -> None:
        self.__uid = __uid
        return
    
    
    def set_st25tb_data_type(self, __st25tb_data_type: str) -> None:
        self.__st25tb_data_type = __st25tb_data_type
        return
    
    
    def add_block_to_matrix(self, __block: str) -> None:
        self.__block_matrix.append(__block)
        return
    
    
    def set_system_otp_block(self, __system_otp_block: str) -> None:
        self.__system_otp_block = __system_otp_block
        return
    
    
    def __repr__(self) -> str:
        representation: str = self.__file_type + " v" + self.__file_type_version + " - " + self.__device_type + "\n"
        representation += "UID: " + self.__uid + "\n"
        representation += "Data Type: " + self.__st25tb_data_type + "\n"

        spacing: str = "=" * 20
        representation += spacing + "\n"

        for i in range(len(self.__block_matrix)):
            representation += (3 - len(str(i))) * " " + str(i) + " | " + self.__block_matrix[i] + "\n"
        
        representation += "OTP | " + self.__system_otp_block + "\n"
        representation += spacing
        return representation