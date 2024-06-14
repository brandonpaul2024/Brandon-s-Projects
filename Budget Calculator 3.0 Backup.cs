using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics.Eventing.Reader;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Budget_Calculator_3._0
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
      
        private void button1_Click(object sender, EventArgs e)
        {
            textBox13.Text = Convert.ToString(Convert.ToInt32(textBox4.Text) + (Convert.ToInt32(textBox5.Text) + (Convert.ToInt32(textBox6.Text) + (Convert.ToInt32(textBox32.Text) + (Convert.ToInt32(textBox34.Text) + (Convert.ToInt32(textBox36.Text) + (Convert.ToInt32(textBox38.Text) + (Convert.ToInt32(textBox40.Text)))))))));
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = string.Empty;
            textBox2.Text = string.Empty;
            textBox3.Text = string.Empty;
            textBox4.Text = 0.ToString();
            textBox5.Text = 0.ToString();
            textBox6.Text = 0.ToString(); 
            textBox7.Text = string.Empty;
            textBox8.Text = string.Empty;
            textBox9.Text = string.Empty;
            textBox10.Text = 0.ToString();
            textBox11.Text = 0.ToString();
            textBox12.Text = 0.ToString();
            textBox13.Text = 0.ToString();
            textBox14.Text = 0.ToString();
            textBox15.Text = 0.ToString();
            textBox16.Text = string.Empty;
            textBox17.Text = string.Empty;
            textBox18.Text = string.Empty; 
            textBox19.Text = string.Empty;
            textBox20.Text = string.Empty;
            textBox21.Text = 0.ToString();
            textBox22.Text = 0.ToString();
            textBox23.Text = 0.ToString();
            textBox24.Text = 0.ToString();
            textBox25.Text = 0.ToString();
            textBox26.Text = 0.ToString();
            textBox27.Text = string.Empty;
            textBox28.Text = 0.ToString();
            textBox29.Text = string.Empty;
            textBox30.Text = 0.ToString();
            textBox31.Text = string.Empty;
            textBox32.Text = 0.ToString();
            textBox33.Text = string.Empty;
            textBox34.Text = 0.ToString();
            textBox35.Text = string.Empty;
            textBox36.Text = 0.ToString();
            textBox37.Text = string.Empty;
            textBox38.Text = 0.ToString();
            textBox39.Text = string.Empty;
            textBox40.Text = 0.ToString();
            textBox41.Text = 0.ToString();
            textBox42.Text = 0.ToString();
            textBox43.Text = string.Empty;
            textBox44.Text = string.Empty;
            textBox45.Text = 0.ToString();
            textBox46.Text = 0.ToString();
            textBox47.Text = 0.ToString();

           
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
          
        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void textBox13_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void textBox15_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void label14_Click(object sender, EventArgs e)
        {
            
        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void textBox43_TextChanged(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox26.Text = Convert.ToString(Convert.ToInt32(textBox21.Text) + (Convert.ToInt32(textBox22.Text) + (Convert.ToInt32(textBox23.Text) + (Convert.ToInt32(textBox24.Text) + (Convert.ToInt32(textBox25.Text) + (Convert.ToInt32(textBox28.Text) + (Convert.ToInt32(textBox30.Text))))))));
        }

        private void button5_Click(object sender, EventArgs e)
        {
            textBox15.Text = Convert.ToString(Convert.ToInt32(textBox10.Text) + (Convert.ToInt32(textBox11.Text) + (Convert.ToInt32(textBox12.Text) + (Convert.ToInt32(textBox41.Text) + (Convert.ToInt32(textBox42.Text) - (Convert.ToInt32(textBox4.Text) + (Convert.ToInt32(textBox5.Text) + (Convert.ToInt32(textBox6.Text) + (Convert.ToInt32(textBox32.Text) + (Convert.ToInt32(textBox34.Text) + (Convert.ToInt32(textBox36.Text) + (Convert.ToInt32(textBox38.Text) + (Convert.ToInt32(textBox40.Text) + (Convert.ToInt32(textBox21.Text) + (Convert.ToInt32(textBox22.Text) + (Convert.ToInt32(textBox23.Text) + (Convert.ToInt32(textBox24.Text) + (Convert.ToInt32(textBox25.Text) + (Convert.ToInt32(textBox28.Text) + (Convert.ToInt32(textBox30.Text)))))))))))))))))))));
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox14.Text = Convert.ToString(Convert.ToInt32(textBox10.Text) + (Convert.ToInt32(textBox11.Text) + (Convert.ToInt32(textBox12.Text) + (Convert.ToInt32(textBox41.Text) + (Convert.ToInt32(textBox42.Text))))));
        }

        private void button7_Click(object sender, EventArgs e)
        {
            textBox47.Text = Convert.ToString(Convert.ToInt32(textBox45.Text) / (Convert.ToInt32(textBox46.Text)));
        }

        private void button8_Click(object sender, EventArgs e)
        {
            textBox1.Text = string.Empty;
            textBox2.Text = string.Empty;
            textBox3.Text = string.Empty;
            textBox39.Text = string.Empty;
            textBox37.Text = string.Empty;
            textBox35.Text = string.Empty;
            textBox33.Text = string.Empty;
            textBox31.Text = string.Empty;
            textBox4.Text = 0.ToString();
            textBox5.Text = 0.ToString();
            textBox6.Text = 0.ToString();
            textBox32.Text = 0.ToString();
            textBox34.Text = 0.ToString();
            textBox36.Text = 0.ToString();
            textBox38.Text = 0.ToString();
            textBox40.Text = 0.ToString();
            textBox13.Text = 0.ToString();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            textBox16.Text = string.Empty;
            textBox17.Text = string.Empty;
            textBox18.Text = string.Empty;
            textBox19.Text = string.Empty;
            textBox20.Text = string.Empty;
            textBox27.Text = string.Empty;
            textBox29.Text = string.Empty;
            textBox21.Text = 0.ToString();
            textBox22.Text = 0.ToString();
            textBox23.Text = 0.ToString();
            textBox24.Text = 0.ToString();
            textBox25.Text = 0.ToString();
            textBox26.Text = 0.ToString();
            textBox28.Text = 0.ToString();
            textBox30.Text = 0.ToString();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            textBox10.Text = 0.ToString();
            textBox11.Text = 0.ToString();
            textBox12.Text = 0.ToString();
            textBox14.Text = 0.ToString();
            textBox41.Text = 0.ToString();
            textBox42.Text = 0.ToString();
            textBox7.Text = string.Empty;
            textBox9.Text = string.Empty;
            textBox43.Text = string.Empty;
            textBox44.Text = string.Empty;
            textBox8.Text = string.Empty;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            textBox45.Text = 0.ToString();
            textBox46.Text = 0.ToString();
            textBox47.Text = 0.ToString();
        }

        private void textBox14_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox15_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox39_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox37_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox35_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox33_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox31_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox16_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox17_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox18_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox19_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox20_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox27_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox29_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox8_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox9_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox43_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void textBox44_TextChanged(object sender, EventArgs e)
        {

        }

        private void label17_Click(object sender, EventArgs e)
        {

        }

        private void textBox42_TextChanged(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }

    }

}
