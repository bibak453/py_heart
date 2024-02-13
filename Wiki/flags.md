### Flag names
```c
char *
FlgName(int c)
{
    static char     foo[10];
    switch (c) {
    case 0x00:
        return "<Temporary Event Bit>";
    case 0x01:
        return "<Akari Event Bit>";
    case 0x02:
        return "<Serika Event Bit>";
    case 0x03:
        return "<Tomoko Event Bit>";
    case 0x04:
        return "<Shiho Event Bit?>";
    case 0x06:
        return "<Multi Event Bit?>";
    case 0x08:
        return "<Remi Event Flag>";
    case 0x09:
        return "<Remi Event Counter 2?>";
    case 0x0c:
        return "<Shiho Event Bit>";
    case 0x0d:
        return "<Akari vs Event Flag>";
    case 0x0e:
        return "<Remi Required Event Flag>";
    case 0x0f:
        return "<Other vs Event Flag>";
    case 0x11:
        return "Rio Event Bit";
    case 0x20:
        return "<Tomoko Event Passed>";
    case 0x14:
        return "<Akari Affection>";
    case 0x15:
        return "<Serika Affection>";
    case 0x16:
        return "<Tomoko Affection>";
    case 0x17:
        return "<Shiho Affection>";
    case 0x18:
        return "<Aoi Affection>";
    case 0x19:
        return "<Multi Affection>";
    case 0x1a:
        return "<Kotone Affection>";
    case 0x1b:
        return "<Remi Affection>";
    case 0x1d:
        return "<Rio Affection>";
    case 0x1e:
        return "<Akari Event Count>";
    case 0x1f:
        return "<Serika Event Count>";
    case 0x22:
        return "<Aoi Event Count>";
    case 0x23:
        return "<Multi Event Count>";
    case 0x24:
        return "<Kotone Event Count>";
    case 0x27:
        return "<Rio Event Counter>";
    case 0x29:
        return "<Serika Event Counter>";
    case 0x2a:
        return "<Tomoko Event Counter>";
    case 0x2c:
        return "<Aoi Event Counter>";
    case 0x2d:
        return "<Multi Event Counter>";
    case 0x2e:
        return "<Kotone Event Counter>";
    case 0x2f:
        return "<Remi Event Counter>";
    case 0x33:
        return "<Serika Event Counter 2>";
    case 0x34:
        return "<Tomoko Event Counter 2>";
    case 0x35:
        return "<Aoi Event Counter 2>";
    case 0x37:
        return "<Multi Event Counter 2>";
    case 0x38:
        return "<Kotone Event Counter 2>";
    case 0x39:
        return "<Remi Event Counter 2>";
    case 0x3b:
        return "<Rio Event Counter>";
    case 0x3e:
        return "<Tomoko Event Counter 3>";
    case 0x42:
        return "<Kotone Event Counter 3>";
    case 0x4c:
        return "<Kotone Event Counter 4>";
    case 0x50:
        return "<Ending Flag 1>";
    case 0x51:
        return "<Ending Flag 2>";
    case 0xa6:
        return "<Action Flag for the Day?>";
    case 0xab:
        return "<Date Counter>";
    case 0xac:
        return "<After-School Movement Position Flag>?";
    case 0xad:
        return "<Day Counter>";
    case 0xae:
        return "<Time Counter>";
    case 0xaf:
        return "<After-School Movement Amount Counter>?";
    }
    sprintf(foo, "flg:%02x", c);
    return foo;
}
```

### Flags System

---

`SetFlag a6 01`: This command sets the second parameter to the flag address specified by the first parameter.

---

`FlagAdd 1d 03`: This command adds the amount of the second parameter to the flag address specified by the first parameter.

---

`FlagSub 18 02`: This command subtracts the amount of the second parameter from the flag address specified by the first parameter.

---

`FlagAdd62 af 01`: This command does the same thing as `FlagAdd`.

---

`FlagSetBit 04 02 01`: If the third parameter is set to 1, then:

```c
state->flag[c[1]] |= (1 << c[2]);
```

but if it's set to zero, then:

```c
state->flag[c[1]] &= ~(1 << c[2]);
```
NOTE: Need to figure out what flags are used as persistent values. Because each route after completing it is probably set to true if completed so we can trigger a congratulation message.