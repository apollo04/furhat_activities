import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { useQuery, UseQueryResult } from 'react-query';
import { UserProfile } from 'types/generated';
import { clearTokens } from 'utils/storage-helper';

export default function useUserProfile({
  enabled,
}: {
  enabled: boolean;
}): UseQueryResult<
  AxiosResponse<UserProfile>,
  AxiosError<{ message: string }>
> {
  const client = useClient();

  const getUserProfile = () => {
    return client.get(`profile`);
  };

  return useQuery(['userProfile', enabled], getUserProfile, {
    enabled,
    retry: false,
    refetchOnMount: false,
    refetchOnWindowFocus: false,
    onError: () => {
      clearTokens();
    },
  });
}
