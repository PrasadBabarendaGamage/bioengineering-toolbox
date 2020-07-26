# Screen FAQ

Install screen on remote machine. After you ssh in, type:
```bash
screen -S insert_name_of_session_here
```

You'll get a welcome message, then you'll be back at a prompt. From
there type your command to start whatever app you want. Once it's
running, press Ctrl-a (control and a at the same time), then press d.
These keystrokes does what's called detaching the screen session.
After detaching, you'll be back at a command prompt. From there you can
logout. The app you started in the screen session keeps on running in the 
background.

To re-attach to your screen session: ssh in, then at a terminal prompt
type:
```bash
screen -list
```
This will show all the remote terminal sessions. Copy the session name of the
 screen you are interested it. Re-attach the screen by typing
in
```bash
screen -r session_name
```



