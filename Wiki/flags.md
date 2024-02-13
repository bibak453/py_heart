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
NOTE: Need to figure out what flags are used as persistend values. Because each route after completing it is probably set to true if completed so we can triger a congratulation messeage from the devs.