Feature('Admin fix Test')

Scenario('fix', (I)=>{
    I.amOnPage('http://localhost:8443/app/admin/')
    I.see('Adsrental Administration')
    I.fillField('input[name="username"]', 'volshebnyi@gmail.com')
    I.fillField('input[name="password"]', 'team17')
    I.click('Log in')
    I.see('Dashboard')
    I.click('Lead accounts')
    I.see('Select lead account to change')
    I.click('Report new issue')
    I.see('Report issue for')
    I.fillField('select[name="issue_type"]', 'Ban Account Request')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Report')
    I.checkOption('input[name="_selected_action"')
    I.click('Fix')
    I.see('Fix Ban Account')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Fix')
    I.see('Fix')
    I.click('Resolve / Reject as admin')
    I.see('Resolve Ban Accoun')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Resolve')
    I.see('New value')
    I.click('Home')
    I.see('Dashboard')
    I.click('Lead accounts')
    I.see('Select lead account to change')
    I.click('Report new issue')
    I.see('Report issue for')
    I.fillField('select[name="issue_type"]', 'Security Checkpoint')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Report')
    I.checkOption('input[name="_selected_action"')
    I.click('Fix')
    I.see('Fix Security Checkpoint')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Fix')
    I.see('Fix')
    I.click('Resolve / Reject as admin')
    I.see('Resolve Security Checkpoint')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Resolve')
    I.see('New value')
    I.click('Home')
    I.see('Dashboard')
    I.click('Lead accounts')
    I.see('Select lead account to change')
    I.click('Report new issue')
    I.see('Report issue for')
    I.fillField('select[name="issue_type"]', 'Missing Payment')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Report')
    I.checkOption('input[name="_selected_action"')
    I.click('Fix')
    I.see('Fix Missing Payment')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Fix')
    I.see('Fix Missing Payment ')
    I.click('Resolve / Reject as admin')
    I.see('Resolve Missing Payment')
    I.fillField('textarea[name="note"]', 'sffsffsswd')
    I.click('Resolve')
    I.see('New value')



});
