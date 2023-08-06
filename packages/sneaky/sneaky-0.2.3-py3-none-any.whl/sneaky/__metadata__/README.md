# sneaky

<badges>[![version](https://img.shields.io/pypi/v/sneaky.svg)](https://pypi.org/project/sneaky/)
[![license](https://img.shields.io/pypi/l/sneaky.svg)](https://pypi.org/project/sneaky/)
[![pyversions](https://img.shields.io/pypi/pyversions/sneaky.svg)](https://pypi.org/project/sneaky/)  
[![powered](https://img.shields.io/badge/Say-Thanks-ddddff.svg)](https://saythanks.io/to/foxe6)
[![donate](https://img.shields.io/badge/Donate-Paypal-0070ba.svg)](https://paypal.me/foxe6)
[![made](https://img.shields.io/badge/Made%20with-PyCharm-red.svg)](https://paypal.me/foxe6)
</badges>

<i>A sneaky web bot based on Selenium driven by ChromeDriver equipped with undetected-chromedriver (as bot detection bypass), Buster (as a reCAPTCHA solver), eavesdropper (as network traffic monitor), vpncmd (as free VPN rotator) let you breach the Internet as you please.</i>

# sneaky

```
sneaky
|---- SNEAKY()
|   |---- traffic
|   |---- request_traffic
|   |---- response_traffic
|   |---- capture_traffic()
|   |---- capture_request_traffic()
|   |---- capture_response_traffic()
|   |---- stop_capture_traffic()
|   |---- stop_capture_request_traffic()
|   |---- stop_capture_response_traffic()
|   |---- clear_traffic()
|   |---- clear_request_traffic()
|   |---- clear_response_traffic()
|   |---- quit()
|   |---- vpncmd # see https://github.com/foxe6/vpncmd#hierarchy
|   '---- driver
|       |---- wait()
|       |---- sleep_random()
|       |---- format_element()
|       |---- print_element()
|       |---- pretty_format_element()
|       |---- pretty_print_element()
|       |---- get_console_log()
|       |---- is_xpath()
|       |---- exist()
|       |---- expand_shadow_dom()
|       |---- xpath()
|       |---- querySelectorAll()
|       |---- get_client_viewport_size()
|       |---- move_by_offset()
|       |---- move_to_xy()
|       |---- move_to_element()
|       |---- click()
|       |---- send_input()
|       |---- mimic_move_to_random_xy()
|       |---- mimic_move_to_xy()
|       |---- mimic_move_to_element()
|       |---- mimic_click_xy()
|       |---- mimic_click()
|       |---- mimic_send_chord()
|       '---- mimic_send_input()
'---- Keys()
    |---- chord()
    |   |---- keys
    |   |---- actions()
    |   '---- perform()
    |---- pause()
    |   |---- sec
    |   '---- pause()
    '---- pause_random()
        |---- sec
        '---- pause()
```

# Demo

[![sneaky](https://img.youtube.com/vi/yEm3Sbm30js/0.jpg)](https://www.youtube.com/watch?v=yEm3Sbm30js)

# Example

## python
See `test`.