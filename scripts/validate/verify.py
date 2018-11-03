import re



def validateUsername(fieldname,request):
    if checkforEmpty(request[fieldname]):
        return False
    if checkforInvalidLength(request[fieldname]):
        return False
    if checkforWhiteSpaces(request[fieldname]):
        return False
    
    return 'validating username'

def validatePassword(fieldname,request):
    if checkforEmpty(request[fieldname]):
        return False
    if checkforInvalidLength(request[fieldname]):
        return False
    if checkforWhiteSpaces(request[fieldname]):
        return False
    
    return 'validating Password'

def verifyPassword(fieldname,request):
    if checkforEmpty(request[fieldname]):
        return False
    if request[fieldname]!=request['password']:
        return False

def validateEmail(fieldname,request):
    
    if (len(request[fieldname])>0):
        print (request[fieldname])
        regExpression= re.compile('[\.@]')

        if len((regExpression.findall(request[fieldname])))!=2:
            print(1)
            return False
        if checkforInvalidLength(request[fieldname]):
            print(2)
            return False
        if checkforWhiteSpaces(request[fieldname]):
            print(3)
            return False
        

def checkforEmpty(field):

    if field=='':
        return True
    else:
        return False

def checkforInvalidLength(field):
    if len(field)<3 or len(field)>20:
        return True

def checkforWhiteSpaces(field):
    reg= re.compile('\s') 
    
    if  len(reg.findall(field))>0:
        return True
    else:
        return False    
    

def validationDictionary():
    return {
        'username': validateUsername,
        'password': validatePassword,
        'password_verify': verifyPassword,
        'email':  validateEmail,
        }