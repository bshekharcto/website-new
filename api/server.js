const express = require('express');
const cors = require('cors');
const nodemailer = require('nodemailer');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5000;

// Create transporter
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST || 'smtp.gmail.com',
  port: parseInt(process.env.SMTP_PORT || '587'),
  secure: process.env.SMTP_SECURE === 'true', // true for 465, false for other ports
  auth: {
    user: process.env.SMTP_USER || '',
    pass: process.env.SMTP_PASS || '',
  },
});

// Verify connection configuration
if (process.env.SMTP_USER && process.env.SMTP_PASS) {
  transporter.verify(function (error, success) {
    if (error) {
      console.log('SMTP Connection Warning: SMTP server connection not configured or incorrect.', error.message);
    } else {
      console.log('SMTP Connection Success: Server is ready to take messages');
    }
  });
} else {
  console.log('SMTP Connection Warning: SMTP_USER and SMTP_PASS are not configured in environment or .env file. Outgoing mail will be simulated in the console logs.');
}

app.post('/api/demo-request', async (req, res) => {
  const { name, email, company, phone, usecase, notes } = req.body;

  console.log('\n=================== NEW DEMO REQUEST ===================');
  console.log(`Timestamp: ${new Date().toISOString()}`);
  console.log(`Full Name: ${name}`);
  console.log(`Work Email: ${email}`);
  console.log(`Company: ${company}`);
  console.log(`Phone Number: ${phone}`);
  console.log(`Primary Asset Class: ${usecase}`);
  console.log(`Project Scale / Notes: ${notes || 'None'}`);
  console.log('========================================================\n');

  const receiverEmail = process.env.RECEIVER_EMAIL || 'info@cognecto.com';
  
  const subject = `Get Started / Request Demo - ${company}`;
  const textBody = `Hello Cognecto Team,

I would like to request a demo / get started with Cognecto.

Here are the contact details:
--------------------------------------------------
Full Name: ${name}
Work Email: ${email}
Company: ${company}
Phone Number: ${phone}
Primary Asset Class: ${usecase}
Project Scale / Notes: ${notes}
--------------------------------------------------

Please contact this lead to schedule a sandbox demonstration.

Best regards,
Cognecto Platform Lead Ingestion`;

  const htmlBody = `
    <h3>Get Started / Request Demo</h3>
    <p>Hello Cognecto Team,</p>
    <p>A new demo request has been submitted:</p>
    <table border="1" cellpadding="6" style="border-collapse: collapse; font-family: sans-serif;">
      <tr><td><strong>Full Name</strong></td><td>${name}</td></tr>
      <tr><td><strong>Work Email</strong></td><td>${email}</td></tr>
      <tr><td><strong>Company</strong></td><td>${company}</td></tr>
      <tr><td><strong>Phone Number</strong></td><td>${phone}</td></tr>
      <tr><td><strong>Primary Asset Class</strong></td><td>${usecase}</td></tr>
      <tr><td><strong>Project Scale / Notes</strong></td><td>${notes || 'None'}</td></tr>
    </table>
    <p>Please contact this lead to schedule a sandbox demonstration.</p>
  `;

  // If SMTP is not configured, simulate success and notify in console
  if (!process.env.SMTP_USER || !process.env.SMTP_PASS) {
    console.log('[SIMULATOR] Email simulation active (SMTP credentials missing). Request processed successfully.');
    return res.status(200).json({ 
      success: true, 
      message: 'Request received. Simulated delivery successfully (SMTP not configured).' 
    });
  }

  try {
    const info = await transporter.sendMail({
      from: `"Cognecto Website" <${process.env.SMTP_USER}>`,
      to: receiverEmail,
      subject: subject,
      text: textBody,
      html: htmlBody,
    });

    console.log('Email sent successfully:', info.messageId);
    res.status(200).json({ success: true, message: 'Request submitted and email sent successfully.' });
  } catch (error) {
    console.error('Failed to send email:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to dispatch email. Please check backend logs or SMTP configuration.',
      error: error.message
    });
  }
});

// Health check endpoint
app.get('/', (req, res) => {
  res.status(200).json({ status: 'ok', service: 'cognecto-api' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
