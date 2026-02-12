# Congregation Care Tracker - Implementation Guide

## 📋 Table of Contents
1. [Hosting Options](#hosting-options)
2. [Quick Start Guide](#quick-start-guide)
3. [Step-by-Step Setup](#step-by-step-setup)
4. [Standard Operating Procedures (SOPs)](#standard-operating-procedures)
5. [Training Materials](#training-materials)
6. [Troubleshooting](#troubleshooting)

---

## 🌐 Hosting Options

### Option 1: Free Web Hosting (RECOMMENDED)
**Best for: Small teams, easy access from any device**

#### Using GitHub Pages (100% Free, No Coding Required)

**What you'll need:**
- A free GitHub account
- 10 minutes of setup time

**Pros:**
- Completely free
- Works on any device (phone, tablet, computer)
- Automatic data storage (persists between sessions)
- No maintenance required
- Secure (https://)

**Cons:**
- Publicly accessible URL (but data is stored locally on each user's device)
- Requires internet connection

#### Setup Steps:

1. **Create a GitHub Account** (if you don't have one)
   - Go to https://github.com
   - Click "Sign up"
   - Follow the prompts (use your church email)

2. **Create a New Repository**
   - Click the "+" icon (top right) → "New repository"
   - Name: `care-tracker`
   - Description: "Congregation Care Tracking Tool"
   - Make it **Public**
   - Check "Add a README file"
   - Click "Create repository"

3. **Upload the HTML File**
   - Click "Add file" → "Upload files"
   - Drag and drop the `Congregation_Care_Tracker.html` file
   - Rename it to `index.html` (important!)
   - Click "Commit changes"

4. **Enable GitHub Pages**
   - Go to Settings (top of your repository)
   - Scroll down to "Pages" (left sidebar)
   - Under "Source", select "main" branch
   - Click "Save"
   - Wait 1-2 minutes

5. **Get Your URL**
   - GitHub will show you a URL like: `https://[your-username].github.io/care-tracker/`
   - Share this URL with your pastoral team
   - Bookmark it on everyone's phones/computers

**Security Note:** While the page is public, all data is stored locally on each user's device. No one else can see your prayer requests or visit records.

---

### Option 2: SharePoint/OneDrive (If your church uses Microsoft 365)
**Best for: Churches already using Microsoft tools**

**Setup Steps:**

1. **Upload to SharePoint**
   - Go to your church's SharePoint site
   - Create a new folder: "Care Tracker"
   - Upload `Congregation_Care_Tracker.html`
   - Right-click the file → "Copy link"
   - Share the link with your team

2. **Security Settings**
   - Click "Manage Access"
   - Ensure only pastoral staff have access
   - Set permissions to "Can edit"

**Note:** Data storage works the same way - stored locally on each user's device.

---

### Option 3: Excel Spreadsheet on Shared Drive
**Best for: Teams comfortable with Excel, need offline access**

**Setup Steps:**

1. **Upload to Cloud Storage**
   - OneDrive/SharePoint (Microsoft 365)
   - Google Drive (convert to Google Sheets or keep as Excel)
   - Dropbox

2. **Share with Your Team**
   - Right-click the file → "Share"
   - Add team members by email
   - Set permissions to "Can edit"

3. **Create Desktop Shortcuts**
   - Open the file from the cloud
   - File → Save As → Desktop
   - Creates a shortcut that always opens the latest version

**Pros:**
- Works offline
- Familiar Excel interface
- All data in one file
- Easy to backup

**Cons:**
- Need to manage version conflicts
- Not as mobile-friendly
- Requires Excel or compatible software

---

## 🚀 Quick Start Guide

### For the Web Tool (5-Minute Setup)

1. **Access the Tool**
   - Open the URL in your web browser
   - Bookmark it (⭐ icon in address bar)
   - Add to home screen on mobile devices

2. **First Entry**
   - Click "Prayer Requests" tab
   - Fill out the form
   - Click "Add Prayer Request"
   - Data saves automatically!

3. **View Dashboard**
   - Click "Dashboard" tab
   - See all your statistics
   - Check upcoming follow-ups

### For the Excel Spreadsheet

1. **Open the File**
   - Double-click `Congregation_Care_Tracker.xlsx`
   - Enable editing if prompted

2. **Add Data**
   - Go to "Prayer Requests" tab
   - Add entries in rows below the sample data
   - Use dropdown menus for Status, Category, etc.

3. **View Dashboard**
   - Click "Dashboard" tab
   - Formulas update automatically

---

## 📖 Step-by-Step Setup

### Week 1: Planning & Preparation

**Day 1-2: Team Meeting**
- [ ] Schedule 30-minute team meeting
- [ ] Review tools with pastoral staff
- [ ] Decide: Web tool, Excel, or both?
- [ ] Assign system administrator (who manages access)

**Day 3-4: Customize Tools**
- [ ] Update staff names in dropdowns
- [ ] Adjust categories to match your church's needs
- [ ] Set up hosting (if using web tool)

**Day 5: Test Run**
- [ ] Each team member adds one test entry
- [ ] Verify everyone can access
- [ ] Fix any access issues

### Week 2: Soft Launch

**Day 1: Training Session (30 minutes)**
- [ ] Walk through each feature
- [ ] Have everyone add real data
- [ ] Answer questions

**Day 2-7: Parallel System**
- [ ] Continue old system alongside new tool
- [ ] Enter all new requests in both systems
- [ ] Compare to ensure nothing is missed

### Week 3: Full Implementation

**Day 1: Switch Over**
- [ ] Stop using old system
- [ ] Migrate any open items to new tool
- [ ] Archive old records

**Ongoing: Weekly Check-ins**
- [ ] Review dashboard together
- [ ] Ensure balanced workload
- [ ] Celebrate answered prayers!

---

## 📝 Standard Operating Procedures (SOPs)

### SOP 1: Adding a New Prayer Request

**When to use:** Someone shares a prayer need

**Steps:**
1. Open the Care Tracker (web or Excel)
2. Navigate to "Prayer Requests" tab
3. Fill in required fields:
   - **Name:** Person requesting prayer
   - **Request Summary:** Brief description (1-2 sentences)
   - **Category:** Select from dropdown
   - **Assigned To:** Who will follow up
   - **Status:** Usually "Active" for new requests
   - **Follow-up Date:** When to check in (typically 1 week)
4. Click "Add Prayer Request" (web) or save (Excel)
5. Note in your calendar to follow up on the specified date

**Best Practices:**
- Add requests within 24 hours of receiving them
- Be specific but respectful of privacy
- Set realistic follow-up dates
- Update after each contact

---

### SOP 2: Recording a Hospital Visit

**When to use:** Someone is hospitalized or seriously ill

**Steps:**
1. Open "Hospital & Illness" tab
2. Fill in required fields:
   - **Name:** Person needing care
   - **Situation:** What happened (surgery, illness, etc.)
   - **Location:** Hospital name, room number if known
   - **Severity:** Low/Moderate/High/Critical
   - **Assigned Visitor:** Who will visit
   - **Visit Date:** When the visit is scheduled
   - **Status:** "Needs Scheduling" or "Scheduled"
3. Add the visit record
4. After the visit:
   - Update status to "Completed"
   - Add notes about the visit
   - Schedule next visit if needed

**Best Practices:**
- Visit within 48 hours for high/critical cases
- Coordinate to avoid multiple visitors on same day
- Always add notes after visits
- Update family on prayer list if applicable

---

### SOP 3: Weekly Dashboard Review

**When to use:** Every Monday morning staff meeting (15 minutes)

**Steps:**
1. Open "Dashboard" tab
2. Review statistics together:
   - How many active prayer requests?
   - Any overdue follow-ups?
   - Visit distribution balanced?
3. Check "Upcoming Follow-ups"
   - Assign this week's contacts
   - Discuss any difficult situations
4. Review "Care Assignments"
   - Is workload balanced?
   - Anyone need help?
5. Update prayer list for Sunday service
6. Close in prayer for congregation needs

**Meeting Template:**
```
AGENDA:
1. Dashboard review (5 min)
2. Upcoming follow-ups (5 min)
3. Workload check (2 min)
4. Prayer (3 min)
```

---

### SOP 4: Monthly Data Cleanup

**When to use:** First Monday of each month (20 minutes)

**Steps:**
1. Review all "Active" prayer requests
   - Still ongoing? → Change to "Ongoing"
   - Resolved? → Change to "Answered" or "Closed"
   - No longer relevant? → Close
2. Review "Ongoing" requests
   - Schedule fresh follow-ups
   - Update notes
3. Close completed visit records
   - Ensure notes are complete
   - Archive if needed
4. Celebrate answered prayers!
   - Add to testimony list
   - Share with congregation

---

### SOP 5: Onboarding New Staff Members

**When to use:** New pastor, elder, or deacon joins team

**Time needed:** 20 minutes

**Steps:**

**Before the meeting:**
1. [ ] Add their name to the system (web: edit HTML file; Excel: add to dropdown lists)
2. [ ] Grant access (send link or share file)
3. [ ] Prepare sample data for demonstration

**During the meeting (15 minutes):**
1. **Overview (3 min)**
   - Show dashboard
   - Explain the purpose
   - Show their current assignments (if any)

2. **Adding Data (5 min)**
   - Walk through adding a prayer request
   - Demonstrate adding a visit record
   - Show how to update status

3. **Daily Workflow (5 min)**
   - When to check the system (daily)
   - How to claim assignments
   - How to mark completed items

4. **Practice (2 min)**
   - Have them add a test entry
   - Have them update a status
   - Answer questions

**After the meeting:**
1. [ ] Send quick reference guide (see below)
2. [ ] Assign them a mentor on the team
3. [ ] Check in after one week

**Quick Reference Card:**
```
=================================
CARE TRACKER QUICK REFERENCE
=================================

DAILY:
□ Check dashboard for your assignments
□ Add any new prayer requests
□ Update completed follow-ups

WEEKLY:
□ Review upcoming follow-ups
□ Balance your workload

MONTHLY:
□ Clean up closed requests
□ Update ongoing situations

ACCESS: [Insert your URL or file location]
HELP: Contact [System Admin Name]
=================================
```

---

### SOP 6: Handling Sensitive Information

**When to use:** Always (CRITICAL)

**Guidelines:**

1. **Privacy First**
   - Only include necessary details
   - Use first names only if highly sensitive
   - Don't include medical diagnoses unless relevant
   - Never include information the person wouldn't want shared

2. **Access Control**
   - Only pastoral staff should have access
   - Never screenshot and share
   - Don't discuss entries outside the team
   - Lock devices when not in use

3. **Confidentiality Reminders**
   - Monthly team discussion on confidentiality
   - Annual review of policies
   - New members sign confidentiality agreement

4. **What to Include:**
   ✅ "Struggling with health issues"
   ✅ "Family situation needs prayer"
   ✅ "Job transition"
   
   ❌ "Has Stage 4 cancer"
   ❌ "Going through divorce from John"
   ❌ Specific financial amounts

---

## 🎓 Training Materials

### 5-Minute Tutorial Video Script

*You can record this on your phone and share with team*

**[Scene 1: Dashboard]**
"Welcome to the Congregation Care Tracker! Let me show you how this helps us care for our church family better.

This is the Dashboard - it shows us everything at a glance:
- Active prayer requests
- Scheduled visits  
- Who needs follow-up this week

**[Scene 2: Adding a Prayer Request]**
Let's add a prayer request. Click 'Prayer Requests,' fill in the form:
- Name
- What they need prayer for
- Choose a category
- Assign someone to follow up
- Set a follow-up date

Click 'Add' and it's saved!

**[Scene 3: Checking Assignments]**
Click 'Care Assignments' to see who's handling what. This helps us balance the workload.

**[Scene 4: Updating Status]**
When you follow up, just click 'Mark Answered' or update the status. Easy!

That's it! Questions? Contact [Your Name]."

---

### Printed Quick Start Guide

```
┌─────────────────────────────────────────────┐
│   CONGREGATION CARE TRACKER QUICK START     │
└─────────────────────────────────────────────┘

📱 ACCESS
Web: [Your URL Here]
Excel: [File Location Here]

➕ ADD PRAYER REQUEST
1. Click "Prayer Requests" tab
2. Fill in the form
3. Click "Add"

🏥 ADD VISIT RECORD  
1. Click "Hospital & Illness" tab
2. Fill in the form
3. Click "Add"

✓ UPDATE STATUS
1. Find the item
2. Click status button
3. Done!

📊 VIEW DASHBOARD
Click "Dashboard" to see:
• Statistics
• Your assignments
• Upcoming follow-ups

❓ NEED HELP?
Contact: [Admin Name]
Phone: [Admin Phone]
Email: [Admin Email]
```

---

## 🔧 Troubleshooting

### Web Tool Issues

**Problem: "I can't see my data after closing the browser"**
- **Solution:** Data is stored per-device. Make sure you're using the same browser and device. Don't use "Private/Incognito" mode.

**Problem: "The page won't load"**
- **Solution:** 
  1. Check your internet connection
  2. Try refreshing (Ctrl+R or Cmd+R)
  3. Clear browser cache
  4. Try a different browser

**Problem: "I accidentally deleted something"**
- **Solution:** Unfortunately, deletions are permanent. In the future, change status to "Closed" instead of deleting.

**Problem: "Multiple people edited at the same time"**
- **Solution:** The web tool stores data locally on each device. For shared data, use the Excel version on a shared drive instead.

### Excel Issues

**Problem: "Formulas showing #REF! error"**
- **Solution:** Don't delete rows with formulas. Contact your system admin.

**Problem: "Can't edit the file"**
- **Solution:** Someone else may have it open. Check with your team.

**Problem: "Dropdowns not working"**
- **Solution:** Make sure you're clicking inside the cell, not on the border.

**Problem: "Lost my changes"**
- **Solution:** Always save before closing. Use auto-save if available in your cloud storage.

---

## 📞 Getting Help

### Support Escalation Path

**Level 1: Quick Reference Guide**
- Check the printed guide
- Review this document

**Level 2: System Administrator**
- Contact: [Name]
- Email: [Email]
- Phone: [Phone]
- Response time: 24 hours

**Level 3: Technical Support**
- If using GitHub Pages: GitHub documentation
- If using Microsoft: Microsoft support
- If using Excel: Microsoft Excel support

---

## 🎯 Success Metrics

Track these monthly to measure effectiveness:

- [ ] % of team using the system weekly
- [ ] Average follow-up completion rate  
- [ ] Workload balance (should be within 20% across team)
- [ ] Prayer requests answered/closed
- [ ] Team satisfaction (simple 1-5 scale)

**Monthly Report Template:**
```
CARE TRACKER MONTHLY REPORT
Month: ___________

Active Requests: ___
Visits Completed: ___
Answered Prayers: ___
Average Response Time: ___ days

Team Feedback:
[Ask: What's working? What needs improvement?]

Action Items for Next Month:
1. _______________
2. _______________
3. _______________
```

---

## ✅ Implementation Checklist

### Pre-Launch
- [ ] Choose hosting option
- [ ] Customize staff names
- [ ] Set up access for team
- [ ] Test with sample data
- [ ] Schedule training session

### Launch Week
- [ ] Conduct training
- [ ] Have everyone add test entries
- [ ] Answer questions
- [ ] Begin parallel tracking (old + new)

### First Month
- [ ] Weekly check-ins
- [ ] Address issues quickly
- [ ] Gather feedback
- [ ] Refine processes

### Ongoing
- [ ] Weekly dashboard reviews
- [ ] Monthly data cleanup
- [ ] Quarterly system review
- [ ] Annual privacy policy review

---

## 📚 Additional Resources

### For Web Tool Users
- GitHub Pages Documentation: https://pages.github.com
- Web browser tutorials: YouTube "How to bookmark a page"

### For Excel Users  
- Microsoft Excel Help: https://support.microsoft.com/excel
- Cloud storage sharing guides (OneDrive, Google Drive)

### For Church Leaders
- Digital ministry best practices
- Pastoral care management books
- Privacy and confidentiality guidelines

---

**Questions or Suggestions?**
Contact your system administrator or update this document as you learn what works best for your team!

*Last Updated: [Date]*
*Version: 1.0*
