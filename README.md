# Salsa

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/adharsh/salsa/master)

It's kinda cool that you can probably represent cuban salsa social dance moves as a finite state machine and use it to generate choreo

To generate social dance choreo, just need to traverse the graph and stop when your follower passes out. To run, click on the above button. Click on `Interactive.ipynb`, change step number, dot file to `social.dot` or `social_all_dile_que_no_is_same.dot`, and change `skip_guapea=False` if you're weak

Preferred & interactive way to visualize data:
```bash
xdot social.dot
xdot social_all_dile_que_no_is_same.dot
```

To generate the `social_all_dile_que_no_is_same.dot` file and images, run:
```bash
./update.sh
```

![](imgs/social.png)
![](imgs/social_all_dile_que_no_is_same.png)

Note: Not sure if all dile que no's can be treated the same, hence the two different images above.
