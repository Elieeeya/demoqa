from selenium.webdriver.common.by import By


class MenuForm:
    menu_elements = (By.XPATH, '//div[@class="card mt-4 top-card"][1]')
    menu_form = (By.XPATH, '//div[@class="card mt-4 top-card"][2]')
    menu_alerts = (By.XPATH, '//div[@class="card mt-4 top-card"][3]')
    menu_widget = (By.XPATH, '//div[@class="card mt-4 top-card"][4]')
    menu_interactions = (By.XPATH, '//div[@class="card mt-4 top-card"][5]')
    menu_books_store_application = (By.XPATH, '//div[@class="card mt-4 top-card"][6]')


class ElenetsMenu:
    text_box = (By.XPATH, "//span[contains(text(),'Text Box')]")


class ElementsForm:
    full_name = (By.ID, 'userName')
    email = (By.ID, 'userEmail')
    current_address = (By.ID, 'currentAddress')
    permanent_address = (By.ID, 'permanentAddress')
    button_submit = (By.ID, 'submit')

    # Table
    table_name = (By.XPATH, "//p[@id='name']")
    table_email = (By.XPATH, "//p[@id='email']")
    table_current_address = (By.XPATH, "//p[@id='currentAddress']")
    table_permanent_address = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBox:
    button_plus = (By.XPATH, './/div[@class="rct-options"]/button[1]')
    button_minus = (By.XPATH, './/div[@class="rct-options"]/button[2]')
    icon_page = (By.XPATH, './/span[@class="rct-node-icon"]/*')

    click_home = (By.CLASS_NAME, 'rct-checkbox')
    view_home = (By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]')
    folder_home_open = (By.XPATH, '//div[@id="tree-node"]/ol/li')

    click_desktop = (By.ID, 'tree-node-desktop')
    click_docments = (By.ID, 'tree-node-documents')
    click_downloads = (By.ID, 'tree-node-downloads')

    click_desktop_notes = (By.ID, 'tree-node-notes')
    click_desktop_commands = (By.ID, 'tree-node-commands')

    click_docments_workspace = (By.ID, 'tree-node-workspace')
    click_docments_workspace_react = (By.ID, 'tree-node-react')
    click_docments_workspace_angular = (By.ID, 'tree-node-angular')
    click_docments_workspace_veu = (By.ID, 'tree-node-veu')

    click_docments_office = (By.ID, 'tree-node-office')
    click_docments_office_public = (By.ID, 'tree-node-public')
    click_docments_office_private = (By.ID, 'tree-node-private')
    click_docments_office_classifield = (By.ID, 'tree-node-classified')
    click_docments_office_general = (By.ID, 'tree-node-general')

    click_downloads_word = (By.ID, 'tree-node-wordFile')
    click_downloads_exel = (By.ID, 'tree-node-excelFile')

    text_home = (By.ID, 'result')
    text_home_folder = (By.XPATH, '//span[contains(text(),"home")]')
