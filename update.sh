#!/usr/bin/env bash
sed 's/Dile Que No Position (Right-to-Right)/Dile Que No Position/g' social.dot > social_all_dile_que_no_is_same.dot
dot -Tpng social.dot -o images/social.png
dot -Tpng social_all_dile_que_no_is_same.dot -o images/social_all_dile_que_no_is_same.png
