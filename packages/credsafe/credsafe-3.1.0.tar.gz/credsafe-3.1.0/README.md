# Credentials Safe

<badges>[![version](https://img.shields.io/pypi/v/credsafe.svg)](https://pypi.org/project/credsafe/)
[![license](https://img.shields.io/pypi/l/credsafe.svg)](https://pypi.org/project/credsafe/)
[![pyversions](https://img.shields.io/pypi/pyversions/credsafe.svg)](https://pypi.org/project/credsafe/)  
[![powered](https://img.shields.io/badge/Say-Thanks-ddddff.svg)](https://saythanks.io/to/foxe6)
[![donate](https://img.shields.io/badge/Donate-Paypal-0070ba.svg)](https://paypal.me/foxe6)
[![made](https://img.shields.io/badge/Made%20with-PyCharm-red.svg)](https://paypal.me/foxe6)
</badges>

<i>Store application credentials in keyring with RSA and AES-256.</i>

# Hierarchy

```
credsafe
|---- Agent()
|   |---- set()
|   |---- get()
|   |---- rm()
|   '---- destroy()
|---- AgentV2()
|   |---- set()
|   |---- get()
|   |---- rm()
|   '---- destroy()
'---- AgentV1()
    |---- set()
    |---- get()
    |---- rm()
    '---- destroy()
```

# Example

## python
See `test`.