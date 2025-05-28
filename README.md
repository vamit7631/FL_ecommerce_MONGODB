 .refine(
    (items) => {
      const seen = new Set();
      for (const item of items) {
        if (seen.has(item.country)) return false;
        seen.add(item.country);
      }
      return true;
    },
    {
      message: 'Each country must be unique',
      path: ['country'], // highlights the field in the array
    }
  );
