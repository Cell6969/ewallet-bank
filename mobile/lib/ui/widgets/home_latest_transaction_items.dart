import 'package:bank_sha/shared/theme.dart';
import 'package:flutter/material.dart';

class HomeLatestTransactionItems extends StatelessWidget {
  final String urlIcon;
  final String title;
  final String trxDate;
  final String value;

  const HomeLatestTransactionItems({
    super.key,
    required this.urlIcon,
    required this.title,
    required this.trxDate,
    required this.value,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 18),
      child: Row(
        children: [
          Image.asset(urlIcon, width: 48),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: blackTextStyle.copyWith(
                    fontSize: 16,
                    fontWeight: medium,
                  ),
                ),
                const SizedBox(height: 2),
                Text(trxDate, style: greyTextStyle.copyWith(fontSize: 12)),
              ],
            ),
          ),
          Text(
            value,
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: medium),
          ),
        ],
      ),
    );
  }
}
