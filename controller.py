import user_interface as us_in
import operation as op
import user_interface as ui


def button_click():
    value_a = us_in.operants_1
    value_b = us_in.operants_2
    optration_a_b = us_in.operantions
    if optration_a_b == 1:
        result = op.sum_value(value_a, value_b)
    elif optration_a_b == 2:
        result = op.sub_value(value_a, value_b)
    elif optration_a_b == 3:
        result = op.del_value(value_a, value_b)
    elif optration_a_b == 4:
        result = op.mult_value(value_a, value_b)

    ui.view_result(result)
   
