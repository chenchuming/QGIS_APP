using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace QgisMobileApp
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class RasterView : ContentPage
	{
		public string Url;
		public RasterView (string url)
		{
			InitializeComponent ();
			//NavigationPage.SetHasNavigationBar(this, false);
			IsRunning(true);
			Url = url;
			cntrlWebView.Source = url;
			IsRunning(false);
		}

		public void IsRunning(bool busy)
		{
			activity.IsEnabled = busy;
			activity.IsRunning = busy;
			activity.IsVisible = busy;
		}

        private void OnBack(object sender, EventArgs e)
        {
			Application.Current.MainPage = new NavigationPage(new MainPage());
		}

		
	}
}