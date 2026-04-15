import 'package:bank_sha/shared/theme.dart';
import 'package:bank_sha/ui/widgets/home_latest_transaction_items.dart';
import 'package:bank_sha/ui/widgets/home_service_items.dart';
import 'package:bank_sha/ui/widgets/home_tips_items.dart';
import 'package:bank_sha/ui/widgets/home_user_items.dart';
import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: lightBackgroundColor,
      bottomNavigationBar: BottomAppBar(
        color: whiteColor,
        shape: CircularNotchedRectangle(),
        clipBehavior: Clip.antiAlias,
        notchMargin: 6,
        elevation: 0,
        child: BottomNavigationBar(
          type: BottomNavigationBarType.fixed,
          elevation: 0,
          backgroundColor: whiteColor,
          selectedItemColor: blueColor,
          unselectedItemColor: blackColor,
          showSelectedLabels: true,
          showUnselectedLabels: true,
          selectedLabelStyle: blueTextStyle.copyWith(
            fontSize: 10,
            fontWeight: medium,
          ),
          unselectedLabelStyle: blackTextStyle.copyWith(
            fontSize: 10,
            fontWeight: medium,
          ),
          items: [
            BottomNavigationBarItem(
              icon: Image.asset(
                'assets/ic_overview.png',
                width: 20,
                color: blueColor,
              ),
              label: 'Overview',
            ),
            BottomNavigationBarItem(
              icon: Image.asset('assets/ic_history.png', width: 20),
              label: 'History',
            ),
            BottomNavigationBarItem(
              icon: Image.asset('assets/ic_statistic.png', width: 20),
              label: 'Statistics',
            ),
            BottomNavigationBarItem(
              icon: Image.asset('assets/ic_reward.png', width: 20),
              label: 'Reward',
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        shape: const CircleBorder(),
        backgroundColor: purpleColor,
        child: Image.asset('assets/ic_plus_circle.png', width: 24),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 24),
        children: [
          buildProfile(context),
          buildWalletCard(),
          buildLevel(),
          buildService(),
          buildLatestTransaction(),
          buildSendAgain(),
          buildFriendlyTips(),
        ],
      ),
    );
  }

  Widget buildProfile(BuildContext context) {
    return GestureDetector(
      onTap: () {
        Navigator.pushNamed(context, '/profile');
      },
      child: Container(
        margin: const EdgeInsets.only(top: 40),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Howdy', style: greyTextStyle.copyWith(fontSize: 16)),
                const SizedBox(height: 2),
                Text(
                  'Shania Deb',
                  style: blackTextStyle.copyWith(
                    fontSize: 20,
                    fontWeight: semiBold,
                  ),
                ),
              ],
            ),
            Container(
              width: 60,
              height: 60,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                image: DecorationImage(
                  image: AssetImage('assets/img_profile.png'),
                ),
              ),
              child: Align(
                alignment: Alignment.topRight,
                child: Container(
                  width: 16,
                  height: 16,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: whiteColor,
                  ),
                  child: Center(
                    child: Icon(
                      Icons.check_circle,
                      color: greenColor,
                      size: 14,
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget buildWalletCard() {
    return Container(
      height: 220,
      width: double.infinity,
      margin: const EdgeInsets.only(top: 30),
      padding: const EdgeInsets.all(30),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(28),
        image: const DecorationImage(
          fit: BoxFit.cover,
          image: AssetImage('assets/img_bg_card.png'),
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Shania Deborah',
            style: whiteTextStyle.copyWith(fontSize: 18, fontWeight: medium),
          ),
          const SizedBox(height: 28),
          Text(
            '**** **** **** 1234',
            style: whiteTextStyle.copyWith(
              fontSize: 18,
              fontWeight: medium,
              letterSpacing: 6,
            ),
          ),
          const SizedBox(height: 21),
          Text('Balance', style: whiteTextStyle),
          Text(
            'Rp. 12.500',
            style: whiteTextStyle.copyWith(fontSize: 24, fontWeight: semiBold),
          ),
        ],
      ),
    );
  }

  Widget buildLevel() {
    return Container(
      margin: const EdgeInsets.only(top: 20),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: whiteColor,
      ),
      child: Column(
        children: [
          Row(
            children: [
              Text(
                'Level 1',
                style: blackTextStyle.copyWith(fontWeight: medium),
              ),
              const Spacer(),
              Text(
                '50% ',
                style: greenTextStyle.copyWith(fontWeight: semiBold),
              ),
              Text(
                'of 20.000',
                style: blackTextStyle.copyWith(fontWeight: semiBold),
              ),
            ],
          ),
          const SizedBox(height: 10),
          ClipRRect(
            borderRadius: BorderRadius.circular(55),
            child: LinearProgressIndicator(
              value: 0.55,
              minHeight: 5,
              valueColor: AlwaysStoppedAnimation(greenColor),
              backgroundColor: lightBackgroundColor,
            ),
          ),
        ],
      ),
    );
  }

  Widget buildService() {
    return Container(
      margin: const EdgeInsets.only(top: 30),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Do something',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          const SizedBox(height: 14),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              HomeServiceItems(
                iconUrl: 'assets/ic_topup.png',
                title: 'Top Up',
                onTap: () {},
              ),
              HomeServiceItems(
                iconUrl: 'assets/ic_send.png',
                title: 'Send',
                onTap: () {},
              ),
              HomeServiceItems(
                iconUrl: 'assets/ic_withdraw.png',
                title: 'Withdraw',
                onTap: () {},
              ),
              HomeServiceItems(
                iconUrl: 'assets/ic_more.png',
                title: 'Top Up',
                onTap: () {},
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget buildLatestTransaction() {
    return Container(
      margin: const EdgeInsets.only(top: 30),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Latest Transaction',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          Container(
            padding: const EdgeInsets.all(22),
            margin: EdgeInsets.only(top: 14),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(20),
              color: whiteColor,
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                HomeLatestTransactionItems(
                  urlIcon: 'assets/ic_transaction_cat1.png',
                  title: 'Top Up',
                  trxDate: 'Yesterday',
                  value: '+ Rp. 400.000',
                ),
                HomeLatestTransactionItems(
                  urlIcon: 'assets/ic_transaction_cat2.png',
                  title: 'Top Up',
                  trxDate: 'Yesterday',
                  value: '+ Rp. 400.000',
                ),
                HomeLatestTransactionItems(
                  urlIcon: 'assets/ic_transaction_cat3.png',
                  title: 'Top Up',
                  trxDate: 'Yesterday',
                  value: '+ Rp. 400.000',
                ),
                HomeLatestTransactionItems(
                  urlIcon: 'assets/ic_transaction_cat4.png',
                  title: 'Top Up',
                  trxDate: 'Yesterday',
                  value: '+ Rp. 400.000',
                ),
                HomeLatestTransactionItems(
                  urlIcon: 'assets/ic_transaction_cat5.png',
                  title: 'Top Up',
                  trxDate: 'Yesterday',
                  value: '+ Rp. 400.000',
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget buildSendAgain() {
    return Container(
      margin: EdgeInsets.only(top: 30),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Send Again',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          const SizedBox(height: 14),
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: [
                HomeUserItems(
                  imageUrl: 'assets/img_friend1.png',
                  username: 'john',
                ),
                HomeUserItems(
                  imageUrl: 'assets/img_friend2.png',
                  username: 'sebastian',
                ),
                HomeUserItems(
                  imageUrl: 'assets/img_friend3.png',
                  username: 'budi',
                ),
                HomeUserItems(
                  imageUrl: 'assets/img_friend4.png',
                  username: 'siti',
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget buildFriendlyTips() {
    return Container(
      margin: EdgeInsets.only(top: 30, bottom: 50),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Friendly Tips',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          const SizedBox(height: 14),
          Wrap(
            spacing: 17,
            runSpacing: 18,
            children: [
              HomeTipsItems(
                imageUrl: 'assets/img_tips1.png',
                title: 'Take care of your money',
                url: 'https://www.google.com',
              ),
              HomeTipsItems(
                imageUrl: 'assets/img_tips2.png',
                title: 'Be aware of scams',
                url: 'https://pub.dev',
              ),
              HomeTipsItems(
                imageUrl: 'assets/img_tips3.png',
                title: 'Be aware of scams',
                url: 'https://www.google.com',
              ),
              HomeTipsItems(
                imageUrl: 'assets/img_tips4.png',
                title: 'Don\'t share your PIN',
                url: 'https://www.youtube.com',
              ),
            ],
          ),
        ],
      ),
    );
  }
}
