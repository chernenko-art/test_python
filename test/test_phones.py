import re
from random import randrange


def test_user_field_on_home_page(app):
    user_list = app.user.get_contact_list()
    # element for choose random user
    index = randrange(len(user_list))
    contact_from_home_page = user_list[index]
    contact_from_edit_page = app.user.get_contact_info_from_edit_page(index)
    # assert phone numbers
    assert contact_from_home_page.all_phones_from_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert name
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    # assert lastname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    # assert address
    assert contact_from_home_page.address == contact_from_edit_page.address
    # assert email
    assert contact_from_home_page.all_email_from_page == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    clear_str = re.sub("[() :HWMP-]", "", s)
    return clear_str


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join([contact.email, contact.email2, contact.email3])
