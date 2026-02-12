# Congregation Care Tracker - Complete Implementation Package

## 📦 What's Included

This package contains everything you need to implement a congregation care tracking system for your church. You have two tools to choose from (or use both!):

### 🌐 Web-Based Tool
- **File:** `Congregation_Care_Tracker.html`
- **Best for:** Mobile access, multiple users, easy sharing
- **Hosting:** Can be hosted for free on GitHub Pages, SharePoint, or similar

### 📊 Excel Spreadsheet
- **File:** `Congregation_Care_Tracker.xlsx`
- **Best for:** Offline access, familiar Excel interface, all-in-one file
- **Hosting:** Share via OneDrive, Google Drive, Dropbox, or email

---

## 🚀 Quick Start (5 Minutes)

### Option 1: Web Tool (Recommended)

1. **Test it locally first:**
   - Double-click `Congregation_Care_Tracker.html`
   - Opens in your web browser
   - Try adding a prayer request or visit
   - Data saves automatically!

2. **Host it online (free):**
   - Follow "Option 1: GitHub Pages" in the Implementation Guide
   - Takes about 10 minutes
   - Get a URL like: `https://yourchurch.github.io/care-tracker/`

3. **Share with your team:**
   - Send them the URL
   - Have them bookmark it
   - Done!

### Option 2: Excel Spreadsheet

1. **Open the file:**
   - Double-click `Congregation_Care_Tracker.xlsx`
   - Enable editing if prompted

2. **Upload to cloud storage:**
   - OneDrive, Google Drive, or Dropbox
   - Share with team members (give edit access)

3. **Start using it:**
   - Team members can access from anywhere
   - Changes sync automatically

---

## 📚 Documentation Files

### 1. **Implementation_Guide.md** ⭐ START HERE
- Complete step-by-step setup instructions
- Hosting options (GitHub Pages, SharePoint, Google Drive)
- Week-by-week implementation timeline
- Standard Operating Procedures (SOPs)
- Troubleshooting guide

**Read this first!** It walks you through everything.

### 2. **Quick_Reference_Guide.html**
- One-page printable guide
- Daily workflows
- How to add requests, record visits, update status
- Perfect for keeping at your desk or on your phone

**Action:** Print this for each team member!

### 3. **Video_Tutorial_Script.md**
- Complete script for recording a training video
- Scene-by-scene breakdown (5-7 minutes total)
- Filming tips and equipment recommendations
- Email template to send video to team

**Optional but recommended:** Record a quick video showing your team how to use it!

### 4. **customize_tracker.py**
- Python script to customize staff names
- Updates both web and Excel tools
- Easy to use - just run it and answer prompts

**Use this if:** You want to change the default staff names (Pastor Mike, Elder Tom, etc.)

---

## 🎯 Recommended Implementation Timeline

### Week 1: Setup & Testing
- [ ] Read the Implementation Guide
- [ ] Choose web tool, Excel, or both
- [ ] Customize staff names (run customize_tracker.py)
- [ ] Set up hosting (if using web tool)
- [ ] Test with sample data

### Week 2: Team Training
- [ ] Schedule 30-minute team meeting
- [ ] Print Quick Reference Guides for everyone
- [ ] Walk through adding requests and visits
- [ ] Have each person add one test entry
- [ ] Answer questions

### Week 3: Parallel Run
- [ ] Use both old system and new tool
- [ ] Enter all new cases in both
- [ ] Compare to verify nothing missed
- [ ] Gather feedback from team

### Week 4: Full Launch
- [ ] Stop using old system
- [ ] Migrate remaining open items
- [ ] Set up weekly Monday morning check-ins
- [ ] Celebrate!

---

## 🔧 Customization

### Change Staff Names

**Option 1: Using the Python Script (Easiest)**
```bash
python customize_tracker.py
```
Follow the prompts to enter your staff names.

**Option 2: Manual Editing**

For the **web tool** (HTML file):
1. Open `Congregation_Care_Tracker.html` in a text editor
2. Search for "Pastor Mike"
3. Replace with your staff names
4. Also update the `staff` array in the JavaScript section (near the bottom)

For the **Excel file**:
1. Open the spreadsheet
2. Go to Data → Data Validation
3. Edit the source lists for dropdowns
4. Update staff names in "Care Assignments" sheet

### Add Your Church Information

Edit the Quick Reference Guide:
1. Open `Quick_Reference_Guide.html` in text editor
2. Replace `[INSERT YOUR URL HERE]` with your actual URL
3. Replace `[INSERT NAME]` with system administrator name
4. Replace `[INSERT EMAIL]` and `[INSERT PHONE]`
5. Save and print!

---

## 📋 Standard Operating Procedures (SOPs)

The Implementation Guide includes complete SOPs for:

1. **Adding a Prayer Request** - When someone shares a need
2. **Recording a Hospital Visit** - When someone is hospitalized
3. **Weekly Dashboard Review** - Every Monday morning (15 min)
4. **Monthly Data Cleanup** - First Monday of month (20 min)
5. **Onboarding New Staff** - When someone joins the team
6. **Handling Sensitive Information** - Privacy guidelines

**These are critical!** Make sure everyone on your team reads them.

---

## 🎓 Training Your Team

### Live Training (Recommended)
**Duration:** 30 minutes

**Agenda:**
1. Overview (5 min) - Show the dashboard, explain purpose
2. Demo (10 min) - Add a prayer request, record a visit
3. Hands-on (10 min) - Have everyone add a test entry
4. Q&A (5 min) - Answer questions

**Materials needed:**
- Projector or screen share
- Quick Reference Guide (printed for each person)
- Live access to the tool

### Video Training (Optional)
Use the Video_Tutorial_Script.md to record a 5-minute video.
- Record yourself going through the tool
- Share video link with team
- Great for new hires or review

---

## 🔐 Security & Privacy

### Critical Rules:
1. **Access Control** - Only pastoral staff should have access
2. **Minimal Details** - Only include what's necessary
3. **No Screenshots** - Never share outside the team
4. **Lock Devices** - Always lock when not in use
5. **First Names Only** - For highly sensitive situations

### Data Storage:
- **Web Tool:** Data stored locally on each user's device (not shared)
- **Excel Tool:** Data in the shared file (control access via cloud permissions)

Read the "Handling Sensitive Information" SOP in the Implementation Guide!

---

## ❓ Troubleshooting

### Web Tool Issues

**Can't see my data after closing browser:**
- Data is stored per-device and per-browser
- Don't use Private/Incognito mode
- Use the same browser each time

**Page won't load:**
- Check internet connection
- Try refreshing (Ctrl+R or Cmd+R)
- Try a different browser
- Clear browser cache

**Multiple people editing:**
- Web tool stores data locally on each device
- For true collaboration, use Excel version instead

### Excel Issues

**Can't edit the file:**
- Someone else may have it open
- Check with team members
- Use cloud version for auto-save

**Formulas showing errors:**
- Don't delete rows with formulas
- Contact your system administrator

**Lost changes:**
- Always save before closing
- Enable auto-save in cloud storage

---

## 📞 Getting Help

### Built-in Support
1. Check the Implementation Guide
2. Review the Quick Reference Guide
3. Check Troubleshooting section

### External Support
- **GitHub Pages:** https://pages.github.com/help
- **Microsoft Excel:** https://support.microsoft.com/excel
- **Google Sheets:** https://support.google.com/sheets

### Designate a System Administrator
Choose one person on your team to be the "go-to" person for:
- Granting access to new users
- Answering questions
- Fixing issues
- Updating staff names

---

## ✅ Pre-Launch Checklist

Before going live with your team:

- [ ] Chose web tool, Excel, or both
- [ ] Customized staff names
- [ ] Set up hosting (if using web tool)
- [ ] Tested adding entries
- [ ] Printed Quick Reference Guides
- [ ] Read all SOPs
- [ ] Scheduled training session
- [ ] Designated system administrator
- [ ] Reviewed privacy guidelines
- [ ] Set up weekly Monday morning reviews

---

## 🎉 Success Metrics

Track these monthly to measure success:

- **Adoption Rate:** % of team using it weekly
- **Response Time:** Average days to follow-up
- **Workload Balance:** Cases distributed evenly?
- **Answered Prayers:** How many marked "Answered"?
- **Team Satisfaction:** Simple 1-5 scale survey

Review these as a team each month and celebrate wins!

---

## 📄 File Inventory

| File | Purpose | When to Use |
|------|---------|-------------|
| `Congregation_Care_Tracker.html` | Web-based tracker | Main tool for most teams |
| `Congregation_Care_Tracker.xlsx` | Excel spreadsheet | Alternative or companion tool |
| `Implementation_Guide.md` | Complete setup guide | Read first, reference often |
| `Quick_Reference_Guide.html` | One-page cheat sheet | Print for everyone |
| `Video_Tutorial_Script.md` | Training video script | Optional video creation |
| `customize_tracker.py` | Customization helper | When changing staff names |
| `README.md` | This file | Overview and quick start |

---

## 💡 Pro Tips

1. **Start Simple** - Don't try to migrate all historical data. Start fresh with new requests.

2. **Check Daily** - Make it part of your morning routine to check the dashboard.

3. **Update Immediately** - Add requests right when you hear them, even on your phone.

4. **Weekly Reviews** - Make Monday morning dashboard review a standing meeting.

5. **Celebrate Answers** - Share answered prayers with the congregation (with permission).

6. **Balance Workload** - Use the Care Assignments tab to ensure fair distribution.

7. **Privacy First** - When in doubt, use less detail, not more.

8. **Backup Regularly** - If using Excel, back up monthly. Web tool data is local to each device.

---

## 🚀 Ready to Launch?

1. Read the **Implementation_Guide.md** (start to finish)
2. Choose your hosting option
3. Customize staff names
4. Print **Quick_Reference_Guide.html** for your team
5. Schedule your training session
6. Launch and start caring for your congregation better!

---

## 📧 Questions?

If you have questions about setup or usage:
1. Check the Implementation Guide first
2. Review the Troubleshooting section
3. Reach out to your designated system administrator

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Created for:** Pastoral Care Teams  

**May this tool help you shepherd your flock with excellence!** 🙏
