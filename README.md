# IpConverter
Support IP classes:
- a.b.c.d
- a.b.c
- a.b
- a 

Supported formats:
- **d**(ecimal)
- **h**(exa)
- **o**(catl)
# Help
```sh
./ipconverter.py ip [format]
Format: d,h or o
 ex: ./ipconverter.py 127.0.0.1 o.h => 0177.0x1
 ```

## Examples

| IP            | Format    | Output        |
| -------       | -------   | -------       |
| 127.0.0.1     | o.d       | 0177.1        |
| 127.0.0.1     | h         | 0x7f000001    |
| 8.8.8.8       | d.o.d     | 8.010.2056    |
| 8.8.8.8       | d         | 134744072     |

 
 **Free Software, Hell Yeah!**
