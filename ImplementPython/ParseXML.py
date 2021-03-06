import xml.etree.ElementTree as ET
import os
import traceback
import json


def xml_getter(xml_file_path, xml_string):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    item = root.find(xml_string)
    return item.text


def xml_parser(xml_file_path):
    #return "Ishmeet"
    if os.path.exists("errorFile.txt"):
        os.remove(r"errorFile.txt")

    dict_output = {}

    # Get Admission and Discharge Date
    adm_discharge_value = ""
    adm_discharge_date = r"{http://www.edifecs.com/xdata/200}Loop-2000B/" \
                         r"{http://www.edifecs.com/xdata/200}Loop-2300/" \
                         r"{http://www.edifecs.com/xdata/200}Segment-DTP_1/" \
                         r"{http://www.edifecs.com/xdata/200}Element-1251"
    try:
        adm_discharge_value = xml_getter(xml_file_path, adm_discharge_date)
    except AttributeError:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write("Unable to extract Admit and Discharge Date")
    except Exception:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write(traceback.format_exc())
    dict_output["adm_discharge_value"] = adm_discharge_value
    print(f'Adm and Discharge Date = {dict_output["adm_discharge_value"]}')

    # Member ID
    member_id_value = ""
    member_id_path = r"{http://www.edifecs.com/xdata/200}Loop-2000B/" \
                     r"{http://www.edifecs.com/xdata/200}Loop-2010BA/" \
                     r"{http://www.edifecs.com/xdata/200}Segment-NM1/" \
                     r"{http://www.edifecs.com/xdata/200}Element-67"
    try:
        member_id_value = xml_getter(xml_file_path, member_id_path)
    except AttributeError:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write("Unable to extract MemberID")
    except Exception:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write(traceback.format_exc())
    dict_output["MemberID"] = member_id_value
    print(dict_output["MemberID"])

    # Provider Name (Institution)
    provider_name_value = ""
    provider_name_path = r"{http://www.edifecs.com/xdata/200}Loop-2000A/" \
                         r"{http://www.edifecs.com/xdata/200}Loop-2010AA/" \
                         r"{http://www.edifecs.com/xdata/200}Segment-NM1/" \
                         r"{http://www.edifecs.com/xdata/200}Element-1035"
    try:
        provider_name_value = xml_getter(xml_file_path, provider_name_path)
    except AttributeError:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write("Unable to extract Provider NAme")
    except Exception:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write(traceback.format_exc())
    dict_output["ProviderName"] = provider_name_value
    print(dict_output["ProviderName"])

    # Billed Amount
    billed_amount_value = ""
    billed_amount_path = r"{http://www.edifecs.com/xdata/200}Loop-2000B/" \
                         r"{http://www.edifecs.com/xdata/200}Loop-2300/" \
                         r"{http://www.edifecs.com/xdata/200}Segment-CLM/" \
                         r"{http://www.edifecs.com/xdata/200}Element-782"
    try:
        billed_amount_value = xml_getter(xml_file_path, billed_amount_path)
    except AttributeError:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write("Unable to extract Billed Amount")
    except Exception:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write(traceback.format_exc())
    dict_output["BilledAmount"] = billed_amount_value
    print(dict_output["BilledAmount"])

    # State
    state_value = ""
    state_path = r"{http://www.edifecs.com/xdata/200}Loop-2000A/" \
                 r"{http://www.edifecs.com/xdata/200}Loop-2010AA/" \
                 r"{http://www.edifecs.com/xdata/200}Segment-N4/" \
                 r"{http://www.edifecs.com/xdata/200}Element-156"
    try:
        state_value = xml_getter(xml_file_path, state_path)
    except AttributeError:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write("Unable to extract State")
    except Exception:
        with open("errorFile.txt", 'w') as fileobj:
            fileobj.write(traceback.format_exc())
    dict_output["State"] = state_value
    print(dict_output["State"])

    return json.dumps(dict_output)

# xml_parser(r"C:\Users\ibindra\Desktop\Institutional Data.xml")
