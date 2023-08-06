# smsir

smsir is a Python library for  using SMS web services www.sms.ir

## Installation

Use the package manager [pip](https://pypi.org/project/smsir/) to install smsir.

```bash
pip install smsir
```

## Usage
[Sms.ir sms](https://pypi.org/project/smsir/) webservice python package. 

```python
from smsir import Token, sms

# returns 'TOKEN'
# get UserApiKey and SecretKey values from your panel
Token(UserApiKey='value', SecretKey='value').get_secure_token()

# returns 'geese'
sms().send_by_mobile_number(
    Messages='your message',
 MobileNumbers='receiver number', 
LineNumber='sender number',
Token=TOKEN #get from method Token 
)


```



## License
[MIT](https://github.com/rahimaee/smsir/blob/main/LICENSE)