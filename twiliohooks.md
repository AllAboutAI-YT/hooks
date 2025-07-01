Below is a **10-minute, end-to-end checklist** to get Claude Code texting you through Twilio every time it fires a `Notification` hook.

---

## 1  Create (or log in to) your Twilio account

1. Visit the **Twilio Console** and create a free trial or paid account.
2. On first login Twilio walks you through buying a phone number (or verifying one, if you’re outside the US). Write down:

   * **Account SID**
   * **Auth Token** (or an API-Key pair, but the token is fine for small scripts)
   * **From** phone number (or a *Messaging Service SID* if you prefer that route) ([twilio.com][1])

> **Trial account note:** you must *verify* every destination number in the Console before you can text it.

---

## 2  Set four environment variables

Add these lines to `~/.bashrc`, `~/.zshrc`, or the secrets manager you use:

```bash
export TWILIO_ACCOUNT_SID="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_FROM="+15017122661"     # the Twilio number or MessagingServiceSid
export MY_MOBILE="+15558675310"       # the phone you’ll receive alerts on
```

Reload the shell: `source ~/.zshrc`.

---

## 3  Smoke-test the API from the command line

```bash
curl -X POST https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json \
  --data-urlencode "From=$TWILIO_FROM" \
  --data-urlencode "To=$MY_MOBILE" \
  --data-urlencode "Body=Hello from Claude Code 🎉" \
  -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN
```

A JSON blob with `"status":"queued"` (or `"sent"`) means it worked; check your phone. ([twilio.com][2], [twilio.com][3])

---

## 4  Paste the Notification hook snippet

Open the **/hooks** dialog → *Notification* → “+ Add new hook…”.
Choose **type = command** and paste:

```jsonc
curl -s -X POST https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json \
  --data-urlencode "From=$TWILIO_FROM" \
  --data-urlencode "To=$MY_MOBILE" \
  --data-urlencode "Body=Claude: $(jq -r .message)" \
  -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN
```

(Leave the matcher blank to fire on every notification.)

Save it to *User settings* if you want texts for every project, or *Project settings* if only this repo should buzz you.

---

## 5  Trigger a test notification

The fastest way is to make Claude do something that needs approval—for example:

```text
/allow Claude to open web browser
```

Claude pauses for permission → Notification fires → **you get an SMS** like:

```
Claude: Needs permission to run WebSearch (search for "pytest fixtures")
```

---

## 6  Hardening and extras

| If you want to…                                   | …then do this                                                                                                                               |                                                         |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Hide Auth Token from `ps` output**              | Put the curl script in `~/.claude/hooks/send_sms.sh` and call the script instead of the full command.                                       |                                                         |
| **Send longer messages**                          | Pass \`Body=\$(jq -r .message                                                                                                               | head -c 1590)\` to stay under 1600-character SMS limit. |
| **Use API Keys instead of the master Auth Token** | Create an *API Key & Secret* in Console → export as `TWILIO_API_KEY`/`TWILIO_API_SECRET` → replace `-u $TWILIO_API_KEY:$TWILIO_API_SECRET`. |                                                         |
| **Avoid leaking in shell history**                | Start variable lines with a leading space before `export …`; many shells skip history for commands that begin with a space.                 |                                                         |
| **Throttle flood of alerts**                      | Wrap the curl in a shell script that logs timestamps and bails if called again within, say, 30 seconds.                                     |                                                         |

---

### Recap

1. **Sign up / grab SID, token, & number**
2. **Export env vars** → `$TWILIO_*`
3. **Test curl manually** (confirm SMS arrives)
4. **Drop curl command into a Notification hook**
5. **Trigger a Claude prompt** → phone buzzes

That’s all—Claude Code is now literally in your pocket. 📲

[1]: https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages?utm_source=chatgpt.com "Send SMS and MMS messages | Twilio"
[2]: https://www.twilio.com/en-us/blog/send-sms-twilio-shell-script-curl?utm_source=chatgpt.com "How to Send an SMS from a Shell Script using cURL - Twilio"
[3]: https://www.twilio.com/docs/usage/requests-to-twilio?utm_source=chatgpt.com "Twilio API requests"
