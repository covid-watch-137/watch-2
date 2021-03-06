Feature('Admin MainPage Test')

Scenario('main', (I)=>{
    I.amOnPage('http://localhost:8443/app/admin/')
    I.see('Adsrental Administration')
    I.fillField('input[name="username"]', 'volshebnyi@gmail.com')
    I.fillField('input[name="password"]', 'team17')
    I.click('Log in')
    I.click('Master Report for Facebook Accounts')
    I.see('Select Report LeadAccount to change')
    I.click('Home')
    I.click('Master Report for Amazon Accounts')
    I.see('Select Report LeadAccount to change')
    I.click('Home')
    I.click('Master Report for ACM Google Accounts')
    I.see('Select Report LeadAccount to change')
    I.click('Home')
    I.click('Facebook Screenshot in Needs Approval status')
    I.see('Select Report LeadAccount to change')
    I.click('Home')
    I.click('Google accounts in Needs Approval status')
    I.see('Select Report LeadAccount to change')
    I.click('Home')
    I.click('Check Report for current month')
    I.see('Select Lead History Month to change')
    I.click('Home')
    I.click('Check Report for previous month')
    I.waitForElement('body', 60)
    I.see('Select Lead History Month to change')
    I.click('Home')
    I.click('Devices shipped this week (06 May 2019 - 06 May 2019)')
    I.see('Select Report Lead to change')
    I.click('Home')
    I.click('Devices shipped previous week (29 Apr 2019 - 05 May 2019')
    I.see('Select Report Lead to change')
    I.click('Home')
    I.click('Devices shipped this month (01 May 2019 - 06 May 2019')
    I.see('Select Report Lead to change')
    I.click('Home')
    I.click('Charge back leads')
    I.see('Select Report Lead to change')
    I.click('Home')
    I.click('Bundler payments report preview')
    I.see('Summary')
    I.click('Admin')
    I.click('Banned lead accounts last 30 days')
    I.see('Select lead account to change')
    I.click('Home')
    I.click('Bundler bonuses')
    I.see('Bundler bonuses for')
    I.click('Home')
    I.click('Bundler daily bonuses')
    I.see('Bundler daily bonuses for')
    I.click('Home')
    I.click('Lead Accounts Weekly Report preview')
    I.see('Select date')
    I.click('Admin')
    I.click('Auto Ban Soon report')
    I.see('Lead accounts')
    I.click('Admin')
    I.click('Bundler payments total report')
    I.see('Bundler payments report')
    I.click('Admin')
    I.click('Ban reason report')
    I.see('Ban reason report')
    I.click('Admin')
    I.click('DEBUG: Tunnel down')
    I.see('Select EC2 Instance to change')
    I.click('Home')
    I.click('Admin Documentation')
    I.see('Documentation')
    I.click('Home')
    I.click('FAQ: Lead documentation')
    I.see('adsrental.Lead')
    I.click('Home')
    I.click('FAQ: RaspberryPi documentation')
    I.see('adsrental.RaspberryPi')
    I.click('Home')
    I.click('FAQ: EC2 Instance documentation')
    I.see('adsrental.EC2Instance')
    I.click('Home')
    I.click('Adsrental')
    I.see('Adsrental')
    I.click('Home')
    I.click('EC2 Instances')
    I.see('Select EC2 Instance to change')
    I.click('Home')
    I.click('Lead Histories Month')
    I.see('Select Lead History Month to change')
    I.click('Home')
    I.click('Lead Timestamps')
    I.see('Select Lead Timestamp to change')
    I.click('Home')
    I.click('Read-only Lead Accounts')
    I.see('Select Read-only Lead Account to change')
    I.click('Home')
    I.click('Read-only Leads')
    I.see('Select Read-only Lead to change')
    I.click('Home')
    I.click('Report LeadAccounts')
    I.see('Select Report LeadAccount to change')
    I.click('Home')
    I.click('Report Leads')
    I.see('Select Report Lead to change')
    I.click('Home')
    I.click('Bundler lead stats')
    I.see('Select bundler lead stat to change')
    I.click('Home')
    I.click('Bundler payments')
    I.see('Select bundler payment to change')
    I.click('Home')
    I.click('Bundler payments reports')
    I.see('Select bundler payments report to change')
    I.click('Home')
    I.click('Bundler teams')
    I.see('Select bundler team to change')
    I.click('Home')
    I.click('Bundlers')
    I.see('Select bundler to change')
    I.click('Home')
    I.click('Customer io events')
    I.see('Select customer io event to change')
    I.click('Home')
    I.click('Lead account issue images')
    I.see('Select lead account issue image to change')
    I.click('Home')
    I.click('Lead account issues')
    I.see('Select lead account issue to change')
    I.click('Home')
    I.click('Lead accounts')
    I.see('Select lead account to change')
    I.click('Home')
    I.click('Lead changes')
    I.see('Select lead change to change')
    I.click('Home')
    I.click('Leads')
    I.see('Select lead to change')
    I.click('Home')
    I.click('Raspberry pi sessions')
    I.see('Select raspberry pi session to change')
    I.click('Home')
    I.click('Raspberry pis')
    I.see('Select raspberry pi to change')
    I.click('Home')
    I.click('Users')
    I.see('Select user to change')
    I.click('Home')
    I.click('Vultr instances')
    I.see('Select vultr instance to change')
    I.click('Home')
    I.click('Auth Token')
    I.see('Adsrental Administration')
    I.click('Home')
    I.click('Tokens')
    I.see('Select Token to change')
    I.click('Home')
});
