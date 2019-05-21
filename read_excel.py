import xlrd

# reads the top row in the first sheet of the excel
def getHeader():
    receiverDataBase = xlrd.open_workbook("receivers.xlsx").sheet_by_index(0)
    nrOfReceivers = receiverDataBase.nrows
    nrOfData = receiverDataBase.ncols
    header = []
    for j in range(0,nrOfData):
        header.append(receiverDataBase.cell_value(0,j))

    return header

# reads all other rows in the first sheet of the excel
def getReceivers():
    receiverDataBase = xlrd.open_workbook("Files/receivers.xlsx").sheet_by_index(0)
    nrOfReceivers = receiverDataBase.nrows
    nrOfData = receiverDataBase.ncols
    receivers = []

    for i in range(1,nrOfReceivers):
        receiver = []
        for j in range(0,nrOfData):
            receiver.append(receiverDataBase.cell_value(i,j))
        receivers.append(receiver)

    return receivers
