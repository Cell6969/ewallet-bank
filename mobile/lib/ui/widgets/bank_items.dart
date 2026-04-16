import 'package:bank_sha/shared/theme.dart';
import 'package:flutter/material.dart';

class BankItems extends StatelessWidget {
  final bool isSelected;
  final String title;
  final String imageUrl;

  const BankItems({
    super.key,
    required this.isSelected,
    required this.title,
    required this.imageUrl,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 18),
      padding: const EdgeInsets.all(22),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: whiteColor,
        border: Border.all(
          width: 2,
          color: isSelected ? blueColor : whiteColor,
        ),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Image.asset(imageUrl, height: 30),
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text(
                title,
                style: blackTextStyle.copyWith(
                  fontSize: 16,
                  fontWeight: medium,
                ),
              ),
              const SizedBox(height: 2),
              Text('50 mins', style: greyTextStyle.copyWith(fontSize: 12)),
            ],
          ),
        ],
      ),
    );
  }
}
