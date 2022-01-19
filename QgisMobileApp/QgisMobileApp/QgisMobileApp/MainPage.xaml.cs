using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Xamarin.Essentials;
using Xamarin.Forms;

namespace QgisMobileApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
            activity.IsVisible = false;
            NavigationPage.SetHasNavigationBar(this, false);
        }

        public void IsRunning(bool busy)
        {
            activity.IsEnabled = busy;
            activity.IsRunning = busy;
            activity.IsVisible = busy;
        }
        private void btn_Clicked(object sender, EventArgs e)
        {
            IsRunning(true);

            var url = "https://rasterfile.azurewebsites.net/";
            if (url != null)
            {
                IsRunning(false);
                //Browser.OpenAsync("https://rasterfile.azurewebsites.net/", BrowserLaunchMode.SystemPreferred);
                Application.Current.MainPage = new NavigationPage(new RasterView(url));
            }
            IsRunning(false);
        }
    }
}
