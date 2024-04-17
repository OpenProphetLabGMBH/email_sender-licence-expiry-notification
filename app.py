import os
import argparse
import logging
from dotenv import load_dotenv
from postmarker.core import PostmarkClient



def print_extended(text, color, style=None):
    """Prints the text in the specified color and style."""
    colors = {
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37'
    }
    styles = {
        'bold': '1',
        'underline': '4',
        'normal': '0'
    }
    color_code = colors.get(color, '0')
    style_code = styles.get(style, '0')
    reset_color = '\033[0m'
    print(f"\033[{style_code};{color_code}m{text}{reset_color}")



# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("email_log.log"), logging.StreamHandler()])



# Load environment variables
load_dotenv()



def send_email(to_email):
    api_key = os.getenv('POSTMARK_API_KEY')

    if not api_key:
        logging.error("POSTMARK_API_KEY environment variable is not set.")
        
        print_extended("\n[ERROR] NO POSTMARK API KEY FOUND", "red", "bold")
        print_extended("\nSOLUTION:", "yellow", "underline")
        print_extended("\t1. Go to Postmark app { https://postmarkapp.com }, generate one for the server.", "cyan", "normal")
        print_extended("\t2. Then, come back here and set the POSTMARK_API_KEY environment variable in a .env file.", "cyan", "normal")
        print_extended("\nERROR DETAILS:", "red", "underline")
        raise ValueError("Please set the POSTMARK_API_KEY environment variable in a .env file.")

    
    client = PostmarkClient(server_token=api_key)

    
    email_parameters = {
        "From": "sdatta@prophet.com",
        "To": to_email,
        "TemplateId": 35610397,
        "TemplateAlias": "software-trial-expiring",
        "TemplateModel": {
            "product_url": "https://resolume.com",
            "product_name": "Resolume Arena",
            "project_name": "Gen.Urban",
            "action_url": "https://resolume.com/shop/upgrade.php",
            "renew_extra_info_url": "https://resolume.com/support/dongle",
            "sender_name": "Saurabh Datta (virtual automated agent)"
        }
    }

    print_extended("RESULT:", "yellow", "underline")
    try:
        client.emails.send_with_template(**email_parameters)
        print_extended(f"\tEmail successfully sent to {to_email}", "green", "normal")
        logging.info(f"Email successfully sent to {to_email}")
    except Exception as e:
        print_extended(f"\tFailed to send email: {e}", "red", "normal")
        logging.error(f"Failed to send email: {e}")



def main():
    parser = argparse.ArgumentParser(description="Send templated emails using Postmark.")
    parser.add_argument("--to", required=True, help="Email address of the recipient.")
    args = parser.parse_args()

    send_email(args.to)

    # try:
    #     send_email(args.to)
    # except KeyboardInterrupt:
    #     logging.info("User interrupted the script")
    #     print_extended("User interrupted the script", "magenta", "normal")



if __name__ == '__main__':
    main()
