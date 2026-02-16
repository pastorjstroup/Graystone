#!/usr/bin/env python3
"""
Congregation Care Tracker - Customization Helper

This script helps you customize the care tracker with your church's staff names.
It will update both the web tool and create a customized version.

Usage: python customize_tracker.py
"""

import os
import re

def get_staff_names():
    """Collect staff names from user input."""
    print("\n" + "="*60)
    print("CONGREGATION CARE TRACKER - CUSTOMIZATION")
    print("="*60)
    print("\nLet's set up your pastoral care team!")
    print("Enter the names of your care team members.")
    print("(Press Enter with a blank name when done)\n")
    
    staff = []
    default_names = ['Pastor Mike', 'Elder Tom', 'Elder Sarah', 'Deacon James', 'Deacon Linda']
    
    print("Default names are:", ", ".join(default_names))
    print("\nDo you want to use custom names? (y/n): ", end='')
    use_custom = input().strip().lower()
    
    if use_custom != 'y':
        return default_names
    
    print("\nEnter your staff names (minimum 2, maximum 10):")
    
    for i in range(10):
        name = input(f"  {i+1}. Name (or press Enter if done): ").strip()
        if not name:
            break
        staff.append(name)
    
    if len(staff) < 2:
        print("\n⚠️  You need at least 2 staff members. Using defaults.")
        return default_names
    
    return staff

def get_church_info():
    """Collect church information."""
    print("\n" + "-"*60)
    print("CHURCH INFORMATION (optional - press Enter to skip)")
    print("-"*60)
    
    church_name = input("\nChurch name: ").strip()
    admin_name = input("System administrator name: ").strip()
    admin_email = input("System administrator email: ").strip()
    admin_phone = input("System administrator phone: ").strip()
    
    return {
        'church_name': church_name or 'Your Church',
        'admin_name': admin_name or '[Admin Name]',
        'admin_email': admin_email or '[admin@church.org]',
        'admin_phone': admin_phone or '[Phone Number]'
    }

def create_staff_options_html(staff_names):
    """Create HTML option elements for staff dropdown."""
    return '\n                            '.join([f'<option>{name}</option>' for name in staff_names])

def customize_html(input_file, output_file, staff_names, church_info):
    """Customize the HTML file with new staff names and church info."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create the options HTML
    staff_options = create_staff_options_html(staff_names)
    
    # Replace all instances of staff dropdowns
    # Prayer form
    content = re.sub(
        r'<select id="prayer-assigned">.*?</select>',
        f'<select id="prayer-assigned">\n                            {staff_options}\n                        </select>',
        content,
        flags=re.DOTALL
    )
    
    # Visit form
    content = re.sub(
        r'<select id="visit-assigned">.*?</select>',
        f'<select id="visit-assigned">\n                            {staff_options}\n                        </select>',
        content,
        flags=re.DOTALL
    )
    
    # Update the staff array in JavaScript
    staff_array = ', '.join([f"'{name}'" for name in staff_names])
    content = re.sub(
        r"const staff = \[.*?\];",
        f"const staff = [{staff_array}];",
        content
    )
    
    # Update church name in title if provided
    if church_info['church_name'] != 'Your Church':
        content = content.replace(
            '🙏 Congregation Care Tracker',
            f"🙏 {church_info['church_name']} Care Tracker"
        )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

def customize_quick_reference(input_file, output_file, church_info):
    """Customize the quick reference guide."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace placeholders
    content = content.replace('[INSERT NAME]', church_info['admin_name'])
    content = content.replace('[INSERT EMAIL]', church_info['admin_email'])
    content = content.replace('[INSERT PHONE]', church_info['admin_phone'])
    
    # Add today's date
    from datetime import datetime
    content = content.replace('[INSERT DATE]', datetime.now().strftime('%B %d, %Y'))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Get customization info
    staff_names = get_staff_names()
    church_info = get_church_info()
    
    print("\n" + "="*60)
    print("CREATING CUSTOMIZED FILES...")
    print("="*60)
    
    # File paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_input = os.path.join(script_dir, 'Congregation_Care_Tracker.html')
    html_output = os.path.join(script_dir, 'Congregation_Care_Tracker_Custom.html')
    quick_ref_input = os.path.join(script_dir, 'Quick_Reference_Guide.html')
    quick_ref_output = os.path.join(script_dir, 'Quick_Reference_Guide_Custom.html')
    
    # Check if input files exist
    if not os.path.exists(html_input):
        # Try in outputs directory
        html_input = '/mnt/user-data/outputs/Congregation_Care_Tracker.html'
        html_output = '/mnt/user-data/outputs/Congregation_Care_Tracker_Custom.html'
    
    if not os.path.exists(quick_ref_input):
        quick_ref_input = os.path.join(script_dir, 'Quick_Reference_Guide.html')
        quick_ref_output = '/mnt/user-data/outputs/Quick_Reference_Guide_Custom.html'
    
    try:
        # Customize HTML tracker
        customize_html(html_input, html_output, staff_names, church_info)
        print(f"\n✓ Created customized tracker: {os.path.basename(html_output)}")
        
        # Customize quick reference if it exists
        if os.path.exists(quick_ref_input):
            customize_quick_reference(quick_ref_input, quick_ref_output, church_info)
            print(f"✓ Created customized quick reference: {os.path.basename(quick_ref_output)}")
        
        print("\n" + "="*60)
        print("CUSTOMIZATION COMPLETE!")
        print("="*60)
        print("\nYour customized files are ready to use!")
        print("\nStaff Members:")
        for i, name in enumerate(staff_names, 1):
            print(f"  {i}. {name}")
        
        print(f"\nSystem Administrator: {church_info['admin_name']}")
        
        print("\n" + "="*60)
        print("NEXT STEPS:")
        print("="*60)
        print("1. Open the customized HTML file in a web browser")
        print("2. Upload it to your hosting (GitHub Pages, SharePoint, etc.)")
        print("3. Print the Quick Reference Guide for your team")
        print("4. Share the URL with your pastoral staff")
        print("\nSee the Implementation_Guide.md for detailed instructions!")
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: Could not find input file")
        print(f"   {e}")
        print("\nMake sure the Congregation_Care_Tracker.html file is in the same")
        print("directory as this script, or in /mnt/user-data/outputs/")
    except Exception as e:
        print(f"\n❌ Error during customization: {e}")

if __name__ == '__main__':
    main()
