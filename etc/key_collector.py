import keyboard as kb

kb.wait("ctrl+r")
recorded = kb.record("esc")

for ele in recorded:
    print(ele.event_type)
    print(ele.name)
