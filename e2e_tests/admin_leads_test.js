Feature('Admin Leads Test')

Scenario('leads', (I)=>{
    I.amOnPage('http://localhost:8443/app/admin/')
    I.see('Adsrental Administration')
    I.fillField('input[name="username"]', 'volshebnyi@gmail.com')
    I.fillField('input[name="password"]', 'team17')
    I.click('Log in')
    I.see('Dashboard')
    I.click('Leads')
    I.fillField('input[name="q"', 'Vlad Emelianov ')
    I.click('Search')
    I.checkOption('input[name="_selected_action"]')
    //don't give any message
    I.fillField('select[name="action"]', 'Approve facebook screenshot')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    //don't give anymessage
    I.fillField('select[name="action"]', 'Approve google')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    //don't give anymessage
    I.fillField('select[name="action"]', 'Mark Facebook account as Qualified')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]',  'Mark Facebook Screenshot account as Qualified')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Mark Google account as Qualified')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    //don't give anymessage
    I.fillField('select[name="action"]', 'Mark Amazon account as Qualified')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Mark as disqualified')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Ban lead')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Unban lead')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Ban google account')
    I.click('Go')
    I.see('Choose reason to ban Google account')
    I.click('Home')
    I.see('Dashboard')
    I.click('Leads')
    I.fillField('input[name="q"', 'Vlad Emelianov ')
    I.click('Search')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Unban google account')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Ban facebook account')
    I.click('Go')
    I.see('Choose reason to ban Facebook account')
    I.click('Home')
    I.see('Dashboard')
    I.click('Leads')
    I.fillField('input[name="q"', 'Vlad Emelianov ')
    I.click('Search')
    I.checkOption('input[name="_selected_action"]')
    //don't give anymessage
    I.fillField('select[name="action"]', 'Unban facebook account')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Ban facebook screenshot account')
    I.click('Go')
    I.see('Choose reason to ban Facebook Screenshot account')
    I.click('Home')
    I.see('Dashboard')
    I.click('Leads')
    I.fillField('input[name="q"', 'Vlad Emelianov ')
    I.click('Search')
    I.checkOption('input[name="_selected_action"]')
    //don't give anymessage
    I.fillField('select[name="action"]', 'Unban facebook screenshot account')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Ban amazon account')
    I.click('Go')
    I.see('Choose reason to ban Amazon account')
    I.click('Home')
    I.see('Dashboard')
    I.click('Leads')
    I.fillField('input[name="q"', 'Vlad Emelianov ')
    I.click('Search')
    I.checkOption('input[name="_selected_action"]')
    //don't give anymessage
    I.fillField('select[name="action"]', 'Unban amazon account')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Prepare for teasting')
    I.click('Go')
    I.see('Prepare for reshipment following leads')
    I.click('Home')
    I.see('Dashboard')
    I.click('Leads')
    I.fillField('input[name="q"', 'Vlad Emelianov ')
    I.click('Search')
    I.checkOption('input[name="_selected_action"]')
    //don't give anymessage
    I.fillField('select[name="action"]', 'Touch')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Resstart rasspbery pi')
    I.click('Go')
    I.checkOption('input[name="_selected_action"]')
    I.fillField('select[name="action"]', 'Sync to adsdb')
    I.click('Go')
    
});