import telebot
import google.generativeai as genai

# Diqqat: Bu yerga o'z kalitlaringizni qo'ying
TELEGRAM_TOKEN = "944892092:AAFCtq05u_gxa82r-szQrHXUPXFPkjjYdfY"
GEMINI_KEY = "This quickstart shows you how to install our libraries
and make your first Gemini API request.

## Before you begin

Using the Gemini API requires an API key, you can create one for free to get started.

Create a Gemini API Key

## Install the Google GenAI SDK

### Python

Using Python 3.9+, install the
google-genai package
using the following
pip command:  

    pip install -q -U google-genai

### JavaScript

Using Node.js v18+,
install the
Google Gen AI SDK for TypeScript and JavaScript
using the following
npm command:  

    npm install @google/genai

### Go

Install
google.golang.org/genai in
your module directory using the go get command:  

    go get google.golang.org/genai

### Java

If you're using Maven, you can install
google-genai by adding the
following to your dependencies:  

    <dependencies>
      <dependency>
        <groupId>com.google.genai</groupId>
        <artifactId>google-genai</artifactId>
        <version>1.0.0</version>
      </dependency>
    </dependencies>

### C#

Install
googleapis/go-genai in
your module directory using the dotnet add command  

    dotnet add package Google.GenAI

### Apps Script

1. To create a new Apps Script project, go to script.new.
2. Click Untitled project.
3. Rename the Apps Script project AI Studio and click Rename.
4. Set your API key
   1. At the left, click Project Settings !The icon for project settings.
   2. Under Script Properties click Add script property.
   3. For Property , enter the key name: GEMINI_API_KEY.
   4. For Value, enter the value for the API key.
   5. Click Save script properties.
5. Replace the Code.gs file contents with the following code:

## Make your first request

Here is an example that uses the
generateContent method
to send a request to the Gemini API using the Gemini 2.5 Flash model.

If you set your API key as the
environment variable GEMINI_API_KEY, it will be picked up automatically by the
client when using the Gemini API libraries.
Otherwise you will need to pass your API key as
an argument when initializing the client.

Note that all code samples in the Gemini API docs assume that you have set the
environment variable GEMINI_API_KEY.  

### Python

    from google import genai

    # The client gets the API key from the environment variable GEMINI_API_KEY.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
    )
    print(response.text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";

    // The client gets the API key from the environment variable GEMINI_API_KEY.
    const ai = new GoogleGenAI({});

async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: "Explain how AI works in a few words",
      });
      console.log(response.text);
    }

    main();

### Go

    package main

    import (
        "context"
        "fmt"
        "log"
        "google.golang.org/genai"
    )

    func main() {
        ctx := context.Background()
        // The client gets the API key from the environment variable GEMINI_API_KEY.
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }

        result, err := client.Models.GenerateContent(
            ctx,
            "gemini-3-flash-preview",
            genai.Text("Explain how AI works in a few words"),
            nil,
        )
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(result.Text())
    }

### Java

    package com.example;

    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentResponse;

    public class GenerateTextFromTextInput {
      public static void main(String[] args) {
        // The client gets the API key from the environment variable GEMINI_API_KEY.
        Client client = new Client();

        GenerateContentResponse response =
            client.models.generateContent(
                "gemini-3-flash-preview",
                "Explain how AI works in a few words",
                null);

        System.out.println(response.text());
      }
    }

### C#

    using System.Threading.Tasks;
    using Google.GenAI;
    using Google.GenAI.Types;

    public class GenerateContentSimpleText {
      public static async Task main() {
        // The client gets the API key from the environment variable GEMINI_API_KEY.
        var client = new Client();
        var response = await client.Models.GenerateContentAsync(
          model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
        );
        Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
      }
    }

### Apps Script

    // See https://developers.google.com/apps-script/guides/properties
    // for instructions on how to set the API key.
    const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
    function main() {
      const payload = {
        contents: [
          {
            parts: [
              { text: 'Explain how AI works in a few words' },
            ],
          },
        ],
      };

      const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
      const options = {
        method: 'POST',
        contentType: 'application/json',
        headers: {
          'x-goog-api-key': apiKey,
        },
        payload: JSON.stringify(payload)
      };

      const response = UrlFetchApp.fetch(url, options);
      const data = JSON.parse(response);
      const content = data['candidates'][0]['content']['parts'][0]['text'];
      console.log(content);
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "text": "Explain how AI works in a few words"
              }
            ]
          }
        ]
      }'

## What's next

Now that you made your first API request, you might want to explore the
following guides that show Gemini in action:

- Text generation
- Image generation
- Image understanding"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Xatolik: {e}")

print("Bot ishlamoqda...")
bot.infinity_polling()
