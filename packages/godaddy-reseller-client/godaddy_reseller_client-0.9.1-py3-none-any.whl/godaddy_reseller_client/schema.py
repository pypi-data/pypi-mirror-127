class schema: 
    def __init__(self) -> None:
        pass
    def create_schema_body(self,consent,domain,contactRegistrant,contactAdmin=None,contactBilling=None,
                        contactTech=None,nameServers=None,period=None,privacy=False,renewAuto=True):
        schema = {
            "consent": {
                **consent
            },
            "contactAdmin": {
                **contactAdmin
                },
            "contactBilling": {
                **contactBilling
                },
            "contactRegistrant": {
                **contactRegistrant
                },
            "contactTech": {
                **contactTech
                },
            "domain": domain,
            "privacy": privacy,
            "renewAuto": renewAuto
        }
        if (contactAdmin != None):
            schema = {
                **schema,
                "contactAdmin": contactAdmin
            }
        if (contactBilling != None):
            schema = {
                **schema,
                "contactBilling": contactBilling
            }
            
        if (contactTech != None): 
            schema = {
                **schema,
                "contactTech": contactTech
            }
        if (nameServers != None):
            schema = {
                **schema,
                "nameServers": nameServers
            }
        if (period != None):
            schema = {
                **schema,
                "period": period
            }
        return schema
        
    def create_schema_consent_body(self,agreedAt,agreedBy,agreementKeys):
        consent = {
            "agreedAt": "{}".format(agreedAt),
            "agreedBy": "{}".format(agreedBy),
            "agreementKeys": agreementKeys
            
        }
        return consent
        
    def create_schema_contact_body(self,addressMailing,email,fax,jobTitle,nameFirst,
                                nameLast,nameMiddle,organization,phone):
        contact = {
            **addressMailing,
            "email": "{}".format(email),
            "fax": "{}".format(fax),
            "jobTitle": "{}".format(jobTitle),
            "nameFirst": "{}".format(nameFirst),
            "nameLast": "{}".format(nameLast),
            "nameMiddle": "{}".format(nameMiddle),
            "organization": "{}".format(organization),
            "phone": "{}".format(phone)
        }
        return contact

    def create_schema_contact_address_mailing(self,address1,address2,city,country,postalCode,state):
        mailing_address = {"addressMailing": {
            "address1": "{}".format(address1),
            "address2": "{}".format(address2),
            "city": "{}".format(city),
            "country": "{}".format(country),
            "postalCode": "{}".format(postalCode),
            "state": "{}".format(state)
        }
        }
        return mailing_address
